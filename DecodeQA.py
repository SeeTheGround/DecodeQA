import lookup_dict


P_RASTER = 0 
P_COLLECTION = 1
P_SENSOR = 2
P_BAND = 3
P_RMLOWLBLS = 4

raster = arcpy.GetParameter(P_RASTER)
collection = arcpy.GetParameter(P_COLLECTION)
sensor = arcpy.GetParameter(P_SENSOR)
band = arcpy.GetParameter(P_BAND)
rm_low = arcpy.GetParameter(P_RMLOWLBLS)


# read lookup dictionary

new_file_name = raster.value.split("\\")[-1][:-4] + "_Decoded.TIF"
new_file_name = os.path.join(os.path.dirname(raster.value),new_file_name)
arcpy.AddMessage(f"Raster: {new_file_name}")

out_raster = arcpy.Raster(raster.value)
raster = out_raster
raster.save(new_file_name)
arcpy.AddMessage(f"Raster saved to: {raster.path}")

bit_flags = lookup_dict.bit_flags

# check to ensure raster is not floating/double/complex
vt = int(str(arcpy.GetRasterProperties_management(raster, "VALUETYPE")))
if vt >= 9:
    msg = "ERROR: Data type of input raster must be integer."
    arcpy.AddError(msg)
    sys.exit(msg)
    
# build attribute table
arcpy.BuildRasterAttributeTable_management(raster, "Overwrite")

# add description field to table
arcpy.AddField_management(raster, "Descr", "TEXT", "", "", 500)
fields = ("Value", "Descr")

arcpy.AddMessage(f"re-map input sensor name to qa_values sensor name")
 # re-map input sensor name to qa_values sensor name
if sensor == 'Landsat 4-5':
    sens = 'L45'
elif sensor == 'Landsat 7':
    sens = 'L7'
elif sensor == 'Landsat 8':
    sens = 'L8'
else:
    arcpy.AddError(f"ERROR: Incorrect sensor provided. Input: {sensor}; "
                   "Potential options: Landsat 4-5 | Landsat 7 | Landsat 8")

arcpy.AddMessage(f"Getting Cursor")
raster.save
with arcpy.da.UpdateCursor(os.path.join(raster.path,raster.name), fields) as cursor:
    
    for row in cursor:
        # check all possible bits for match with target value (row[0])
        bit_values = sorted(bit_flags[collection][band][sens].values())
        bit_bool = []
        for bv in bit_values:
            if len(bv) == 1:  # single bit
                bit_bool.append(row[0] & 1 << bv[0] > 0)

            elif len(bv) > 1:  # 2+ bits
                bits = []
                for b in bv:
                    bits.append(row[0] & 1 << b > 0)
                if all(item == True for item in bits):
                    bit_bool.append(True)
                else:
                    bit_bool.append(False)

            else:
                sys.exit("No valid bits found for target band.")

        # create description of each value based upon all possible bits
        true_bits = [i for (i, bb) in zip(bit_values, bit_bool) if bb]

        # if double bits exist, eliminate single bit descriptions,
        #   otherwise, the descriptions will duplicate themselves.
        bb_double = [len(i) > 1 for i in true_bits]
        if any(bb_double):
            # get only the double bits
            dbit_nest = [i for (i, db) in zip(true_bits, bb_double) if db]

            # collapse the bits into a single list
            dbits = [item for sublist in dbit_nest for item in sublist]

            # remove matching single bits out of true_bits list
            tbo = []
            for t in true_bits:
                tb_out = []
                for d in dbits:
                    if t[0] != d or len(t) > 1:
                        tb_out.append(True)
                    else:
                        tb_out.append(False)
                if all(tb_out):
                    tbo.append(t)

            # replace true_bits with filtered list
            true_bits = tbo

        def get_label(bits):
            """
            Generate label for value in attribute table.

            :param bits: <list> List of True or False for bit position
            :return: <str> Attribute label
            """
            if len(bits) == 0:
                if band == 'radsat_qa':
                    return 'No Saturation'

                elif band == 'sr_cloud_qa' or band == 'sr_aerosol':
                    return 'None'

                elif band == 'BQA':
                    return 'Not Determined'

            # build description from all bits represented in value
            desc = []
            for tb in bits:
                k = next(key for key, value in
                         bit_flags[collection][band][sens].items() if value == tb)

                # if 'low' labels are disabled, do not add them here
                if rm_low and band != 'BQA' and 'low' in k.lower():
                    continue

                # if last check, and not radiometric sat, set to 'clear'
                elif rm_low and band == 'BQA' and 'low' in k.lower() and \
                                tb == bits[-1] and \
                                'radiometric' not in k.lower() and \
                        not desc:
                    k = 'Clear'

                # if BQA and bit is low radiometric sat, keep it
                elif rm_low and band == 'BQA' and 'low' in k.lower():
                    if 'radiometric' not in k.lower():
                        continue

                # if radsat_qa, handle differently to make display cleaner
                if band == 'radsat_qa':
                    if not desc:
                        desc = "Band {0} Data Saturation".format(tb[0])

                    else:
                        desc = "{0},{1} Data Saturation".format(
                            desc[:desc.find('Data') - 1], tb[0])

                # string creation for all other bands
                else:
                    if not desc:
                        desc = "{0}".format(k)

                    else:
                        desc += ", {0}".format(k)

            # final check to make sure something was set
            if not desc:
                desc = 'ERROR: bit set incorrectly'

            return desc

        # add desc to row description (row[1])
        try:
            row[1] = get_label(true_bits)
        except UnboundLocalError:
            row[1] = 'ERROR: bit read incorrectly'

        # update table row
        cursor.updateRow(row)
        arcpy.AddMessage(f"Complete")
        arcpy.AddMessage("Adding Raster to current map")
#try:
aprx = arcpy.mp.ArcGISProject('CURRENT')
activeMap = aprx.activeMap
activeMap.addDataFromPath(new_file_name)


#except:
 #   arcpy.AddError("Could not add Raster to current map.")


    
