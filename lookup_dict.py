
bit_flags = {
    "Collection 1": {
        "pixel_qa": {
            "L45": {
                "Fill": [0],
                "Clear": [1],
                "Water": [2],
                "Cloud Shadow": [3],
                "Snow": [4],
                "Cloud": [5],
                "Low Cloud Confidence": [6],
                "Medium Cloud Confidence": [7],
                "High Cloud Confidence": [6, 7]
            },
            "L7": {
                "Fill": [0],
                "Clear": [1],
                "Water": [2],
                "Cloud Shadow": [3],
                "Snow": [4],
                "Cloud": [5],
                "Low Cloud Confidence": [6],
                "Medium Cloud Confidence": [7],
                "High Cloud Confidence": [6, 7]
            },
            "L8": {
                "Fill": [0],
                "Clear": [1],
                "Water": [2],
                "Cloud Shadow": [3],
                "Snow": [4],
                "Cloud": [5],
                "Low Cloud Confidence": [6],
                "Medium Cloud Confidence": [7],
                "High Cloud Confidence": [6, 7],
                "Low Cirrus Confidence": [8],
                "Medium Cirrus Confidence": [9],
                "High Cirrus Confidence": [8, 9],
                "Terrain Occlusion": [10]
            }
        },

        "sr_cloud_qa": {
            "L45": {
                "DDV": [0],
                "Cloud": [1],
                "Cloud Shadow": [2],
                "Adjacent to Cloud": [3],
                "Snow": [4],
                "Water": [5]
            },
            "L7": {
                "DDV": [0],
                "Cloud": [1],
                "Cloud Shadow": [2],
                "Adjacent to Cloud": [3],
                "Snow": [4],
                "Water": [5]
            }
        },

        "radsat_qa": {
            "L45": {
                "Fill": [0],
                "Band 1 Data Saturation": [1],
                "Band 2 Data Saturation": [2],
                "Band 3 Data Saturation": [3],
                "Band 4 Data Saturation": [4],
                "Band 5 Data Saturation": [5],
                "Band 6 Data Saturation": [6],
                "Band 7 Data Saturation": [7]
            },
            "L7": {
                "Fill": [0],
                "Band 1 Data Saturation": [1],
                "Band 2 Data Saturation": [2],
                "Band 3 Data Saturation": [3],
                "Band 4 Data Saturation": [4],
                "Band 5 Data Saturation": [5],
                "Band 6 Data Saturation": [6],
                "Band 7 Data Saturation": [7]
            },
            "L8": {
                "Fill": [0],
                "Band 1 Data Saturation": [1],
                "Band 2 Data Saturation": [2],
                "Band 3 Data Saturation": [3],
                "Band 4 Data Saturation": [4],
                "Band 5 Data Saturation": [5],
                "Band 6 Data Saturation": [6],
                "Band 7 Data Saturation": [7],
                "Band 9 Data Saturation": [9],
                "Band 10 Data Saturation": [10],
                "Band 11 Data Saturation": [11]
            }
        },

        "BQA": {
            "L45": {
                "Fill": [0],
                "Dropped Pixel": [1],
                "Low Radiometric Saturation": [2],
                "Medium Radiometric Saturation": [3],
                "High Radiometric Saturation": [2, 3],
                "Cloud": [4],
                "Low Cloud Confidence": [5],
                "Medium Cloud Confidence": [6],
                "High Cloud Confidence": [5, 6],
                "Low Cloud Shadow Confidence": [7],
                "High Cloud Shadow Confidence": [7, 8],
                "Low Snow/Ice Confidence": [9],
                "High Snow/Ice Confidence": [9, 10]
            },
            "L7": {
                "Fill": [0],
                "Dropped Pixel": [1],
                "Low Radiometric Saturation": [2],
                "Medium Radiometric Saturation": [3],
                "High Radiometric Saturation": [2, 3],
                "Cloud": [4],
                "Low Cloud Confidence": [5],
                "Medium Cloud Confidence": [6],
                "High Cloud Confidence": [5, 6],
                "Low Cloud Shadow Confidence": [7],
                "High Cloud Shadow Confidence": [7, 8],
                "Low Snow/Ice Confidence": [9],
                "High Snow/Ice Confidence": [9, 10]
            },
            "L8": {
                "Fill": [0],
                "Terrain Occlusion": [1],
                "Low Radiometric Saturation": [2],
                "Medium Radiometric Saturation": [3],
                "High Radiometric Saturation": [2, 3],
                "Cloud": [4],
                "Low Cloud Confidence": [5],
                "Medium Cloud Confidence": [6],
                "High Cloud Confidence": [5, 6],
                "Low Cloud Shadow Confidence": [7],
                "High Cloud Shadow Confidence": [7, 8],
                "Low Snow/Ice Confidence": [9],
                "High Snow/Ice Confidence": [9, 10],
                "Low Cirrus Confidence": [11],
                "High Cirrus Confidence": [11, 12]
            }
        },

        "sr_aerosol": {
            "L8": {
                "Fill": [0],
                "Valid Aerosol Retrieval": [1],
                "Water": [2],
                "Cloud or Cirrus": [3],
                "Cloud Shadow": [4],
                "Interpolated Aerosol Retrieval": [5],
                "Low Aerosol": [6],
                "Medium Aerosol": [7],
                "High Aerosol": [6, 7]
            }
        },

        "l2_flags": {
            "L8": {
                "Atmospheric Correction Failed": [0],
                "Land": [1],
                "Sun Glint": [3],
                "High Viewing Zenith Angle": [5],
                "Shallow Water": [6],
                "SeaDAS Cloud": [7],
                "Cloud Shadow": [8],
                "Cloud": [9],
                "Coccolithophores": [10],
                "Turbid Water": [11],
                "High Solar Zenith Angle": [12],
                "Low Water-Leaving Radiance": [14],
                "Chlorophyll-a Calculation Failed": [15],
                "Navigation quality is suspect": [16],
                "Invalid Rrs Value": [18],
                "Max Iterations reached for Aerosol Correction": [19],
                "Moderate sun glint contamination": [20],
                "Invalid Chlorophyll-a Value": [21],
                "Atmospheric Correction Warning": [22],
                "Possible Sea Ice Contamination": [24],
                "Navigation failure": [25],
                "Insufficient Valid Pixels in the Filter": [26],
                "Unused": [2, 4, 13, 17, 23, 27, 28, 29, 30, 31]
            }
        }
    },

    "Collection 2": {
        "pixel_qa": {
            "L45": {
                "Fill": [0],
                "Dilated Cloud": [1],
                "Cloud": [3],
                "Cloud Shadow": [4],
                "Snow": [5],
                "Clear": [6],
                "Water": [7],
                "Low Cloud Confidence": [8],
                "Medium Cloud Confidence": [9],
                "High Cloud Confidence": [8, 9],
                "Low Cloud Shadow Confidence": [10],
                "High Cloud Shadow Confidence": [10, 11],
                "Low Snow/Ice Confidence": [12],
                "High Snow/Ice Confidence": [12, 13]
            },
            "L7": {
                "Fill": [0],
                "Dilated Cloud": [1],
                "Cloud": [3],
                "Cloud Shadow": [4],
                "Snow": [5],
                "Clear": [6],
                "Water": [7],
                "Low Cloud Confidence": [8],
                "Medium Cloud Confidence": [9],
                "High Cloud Confidence": [8, 9],
                "Low Cloud Shadow Confidence": [10],
                "High Cloud Shadow Confidence": [10, 11],
                "Low Snow/Ice Confidence": [12],
                "High Snow/Ice Confidence": [12, 13]
            },
            "L8": {
                "Fill": [0],
                "Dilated Cloud": [1],
                "Cloud": [3],
                "Cloud Shadow": [4],
                "Snow": [5],
                "Clear": [6],
                "Water": [7],
                "Low Cloud Confidence": [8],
                "Medium Cloud Confidence": [9],
                "High Cloud Confidence": [8, 9],
                "Low Cloud Shadow Confidence": [10],
                "High Cloud Shadow Confidence": [10, 11],
                "Low Snow/Ice Confidence": [12],
                "High Snow/Ice Confidence": [12, 13]
            }
        },

        "sr_cloud_qa": {
            "L45": {
                "DDV": [0],
                "Cloud": [1],
                "Cloud Shadow": [2],
                "Adjacent to Cloud": [3],
                "Snow": [4],
                "Water": [5]
            },
            "L7": {
                "DDV": [0],
                "Cloud": [1],
                "Cloud Shadow": [2],
                "Adjacent to Cloud": [3],
                "Snow": [4],
                "Water": [5]
            }
        },

        "radsat_qa": {
            "L45": {
                "Band 1 Data Saturation": [0],
                "Band 2 Data Saturation": [1],
                "Band 3 Data Saturation": [2],
                "Band 4 Data Saturation": [3],
                "Band 5 Data Saturation": [4],
                "Band 6 Data Saturation": [5],
                "Band 7 Data Saturation": [6],
                "Dropped Pixel": [9]
            },
            "L7": {
                "Band 1 Data Saturation": [0],
                "Band 2 Data Saturation": [1],
                "Band 3 Data Saturation": [2],
                "Band 4 Data Saturation": [3],
                "Band 5 Data Saturation": [4],
                "Band 6L Data Saturation": [5],
                "Band 7 Data Saturation": [6],
                "Band 6H Data Saturation": [8],
                "Dropped Pixel": [9]
            },
            "L8": {
                "Band 1 Data Saturation": [0],
                "Band 2 Data Saturation": [1],
                "Band 3 Data Saturation": [2],
                "Band 4 Data Saturation": [3],
                "Band 5 Data Saturation": [4],
                "Band 6 Data Saturation": [5],
                "Band 7 Data Saturation": [6],
                "Band 9 Data Saturation": [8],
                "Terrain Occlusion": [11]
            }
        },

        "BQA": {
            "L45": {
                "Fill": [0],
                "Dilated Cloud": [1],
                "Cloud": [3],
                "Cloud Shadow": [4],
                "Snow": [5],
                "Clear": [6],
                "Water": [7],
                "Low Cloud Confidence": [8],
                "Medium Cloud Confidence": [9],
                "High Cloud Confidence": [8, 9],
                "Low Cloud Shadow Confidence": [10],
                "Medium Cloud Shadow Confidence": [11],
                "High Cloud Shadow Confidence": [10, 11],
                "Low Snow/Ice Confidence": [12],
                "Medium Snow/Ice Confidence": [13],
                "High Snow/Ice Confidence": [12, 13]
            },
            "L7": {
                "Fill": [0],
                "Dilated Cloud": [1],
                "Cloud": [3],
                "Cloud Shadow": [4],
                "Snow": [5],
                "Clear": [6],
                "Water": [7],
                "Low Cloud Confidence": [8],
                "Medium Cloud Confidence": [9],
                "High Cloud Confidence": [8, 9],
                "Low Cloud Shadow Confidence": [10],
                "Medium Cloud Shadow Confidence": [11],
                "High Cloud Shadow Confidence": [10, 11],
                "Low Snow/Ice Confidence": [12],
                "Medium Snow/Ice Confidence": [13],
                "High Snow/Ice Confidence": [12, 13]
            },
            "L8": {
                "Fill": [0],
                "Dilated Cloud": [1],
                "Cirrus": [2],
                "Cloud": [3],
                "Cloud Shadow": [4],
                "Snow": [5],
                "Clear": [6],
                "Water": [7],
                "Low Cloud Confidence": [8],
                "Medium Cloud Confidence": [9],
                "High Cloud Confidence": [8, 9],
                "Low Cloud Shadow Confidence": [10],
                "Medium Cloud Shadow Confidence": [11],
                "High Cloud Shadow Confidence": [10, 11],
                "Low Snow/Ice Confidence": [12],
                "Medium Snow/Ice Confidence": [13],
                "High Snow/Ice Confidence": [12, 13],
                "Low Cirrus Confidence": [14],
                "Medium Cirrus Confidence": [15],
                "High Cirrus Confidence": [14, 15]
            }
        },

        "sr_aerosol": {
            "L8": {
                "Fill": [0],
                "Valid Aerosol Retrieval": [1],
                "Water": [2],
                "Interpolated Aerosol Retrieval": [5],
                "Low Aerosol": [6],
                "Medium Aerosol": [7],
                "High Aerosol": [6, 7]
            }
        }
    }
}
