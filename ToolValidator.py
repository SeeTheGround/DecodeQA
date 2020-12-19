class ToolValidator:
    # Class to add custom behavior and properties to the tool and tool parameters.

    def __init__(self):
        # set self.params for use in other function
        self.params = arcpy.GetParameterInfo()

    def initializeParameters(self):
        # Customize parameter properties. 
        # This gets called when the tool is opened.
        return

    def updateParameters(self):
        if self.params[0].valueAsText and not self.params[1].altered:
            if [c for c in ['_01_', '_C01_'] if
                  c in self.params[0].valueAsText]:
                self.params[1].value = 'Collection 1'
            elif [c for c in ['_02_'] if
                  c in params[0].valueAsText]:
                self.params[1].value = 'Collection 2'

        # Change sensor in drop-down
        if self.params[0].valueAsText and not self.params[2].altered:
            if [s for s in ['LT05', 'LT04'] if
                  s in self.params[0].valueAsText]:
                self.params[2].value = 'Landsat 4-5'

            elif [s for s in ['LE07'] if
                  s in self.params[0].valueAsText]:
                self.params[2].value = 'Landsat 7'

            elif [s for s in ['LC08', 'LT08', 'LO08'] if
                  s in self.params[0].valueAsText]:
                self.params[2].value = 'Landsat 8'

        # Restrict band options based upon sensor
        if self.params[2].valueAsText and not self.params[3].altered:
            if self.params[2].value == 'Landsat 8':
                self.params[3].filter.list = ['BQA',
                                             'pixel_qa',
                                             'radsat_qa',
                                             'sr_aerosol',
                                             'l2_flags']

            elif self.params[2].value == 'Landsat 4-5' or self.params[2].value == 'Landsat 7':
                self.params[3].filter.list = ['BQA',
                                             'pixel_qa',
                                             'radsat_qa',
                                             'sr_cloud_qa']

        # Change band in drop-down
        if self.params[0].valueAsText and not self.params[3].altered:
            if [b for b in ['bqa', 'BQA'] if
                  b in self.params[0].valueAsText]:
                self.params[3].value = 'BQA'
            elif [b for b in ['pixel_qa', 'PIXELQA', 'QA_PIXEL'] if
                  b in self.params[0].valueAsText]:
                self.params[3].value = 'pixel_qa'
            elif [b for b in ['radsat_qa', 'RADSATQA', 'QA_RADSAT'] if
                  b in self.params[0].valueAsText]:
                self.params[3].value = 'radsat_qa'
            elif [b for b in ['sr_aerosol', 'SRAEROSOLQA', 'SR_QA_AEROSOL'] if
                  b in self.params[0].valueAsText]:
                self.params[3].value = 'sr_aerosol'
            elif [b for b in ['sr_cloud_qa', 'SRCLOUDQA', 'SR_CLOUD_QA'] if
                  b in self.params[0].valueAsText]:
                self.params[3].value = 'sr_cloud_qa'
            elif [b for b in ['l2_flags', 'L2_FLAGS'] if
                  b in self.params[0].valueAsText]:
                self.params[3].value = 'l2_flags'
        
        return

    def updateMessages(self):
        # Customize messages for the parameters.
        # This gets called after standard validation.
        return

    # def isLicensed(self):
    #     # set tool isLicensed.
    #     return True
