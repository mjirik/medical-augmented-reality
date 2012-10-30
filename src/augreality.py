#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append("./src/")
import pdb
#  pdb.set_trace();

#import scipy.io

import logging
logger = logging.getLogger(__name__)


import argparse
import numpy as np

#Ahooooooj

class MAR:
    """
    Medical Augmented Reality Class. 
    """
    def __init__(self,device=0):
# zde budou probíhat inicializace
        self.device = device

    def run(self, parametr1=1):
        # Tady bude ležet hlavní kód pro běh
        pass


# --------------------------tests-----------------------------
class Tests(unittest.TestCase):
    def test_t(self):
        pass
    def setUp(self):
        """ Nastavení společných proměnných pro testy  """
        datashape = [220,115,30]
        self.datashape = datashape
        self.rnddata = np.random.rand(datashape[0], datashape[1], datashape[2])
        self.segmcube = np.zeros(datashape)
        self.segmcube[130:190, 40:90,5:15] = 1

#    def test_same_size_input_and_output(self):
#        """Funkce testuje stejnost vstupních a výstupních dat"""
#        outputdata = vesselSegmentation(self.rnddata,self.segmcube)
#        self.assertEqual(outputdata.shape, self.rnddata.shape)


#
#    def test_different_data_and_segmentation_size(self):
#        """ Funkce ověřuje vyhození výjimky při různém velikosti vstpních
#        dat a segmentace """
#        pdb.set_trace();
#        self.assertRaises(Exception, vesselSegmentation, (self.rnddata, self.segmcube[2:,:,:]) )
#
        
        
# --------------------------main------------------------------
if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)
# při vývoji si necháme vypisovat všechny hlášky
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
#   output configureation
    #logging.basicConfig(format='%(asctime)s %(message)s')
    logging.basicConfig(format='%(message)s')

    formatter = logging.Formatter("%(levelname)-5s [%(module)s:%(funcName)s:%(lineno)d] %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)

    logger.addHandler(ch)


    # input parser
    parser = argparse.ArgumentParser(description='Segment vessels from liver')
    parser.add_argument('-p', '--projector', type=str,
            default='1',
            help='*.mat file with variables "data", "segmentation" and "threshod"')
    parser.add_argument('-d', '--debug', action='store_true',
            help='run in debug mode')
    parser.add_argument('-t', '--tests', action='store_true', 
            help='run unittest')
    parser.add_argument('-o', '--outputfile', type=str,
        default='output.mat',help='output file name')
    args = parser.parse_args()


    if args.debug:
        logger.setLevel(logging.DEBUG)

    if args.tests:
        # hack for use argparse and unittest in one module
        sys.argv[1:]=[]
        unittest.main()


#   load all 


    # zastavení chodu programu pro potřeby debugu, 
    # ovládá se klávesou's','c',... 
    # zakomentovat
    pdb.set_trace();

    mar = MAR(args.projector)
    mar.run()

