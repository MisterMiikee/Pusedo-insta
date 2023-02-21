#!/usr/bin/env python3

"""
Intro
"""

import sys
import platform

import cv2 as cv


def rescaleFrame(frame, scale=.75):
    # Works for IMG, VODS, and Live VODS
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def main():
    img = cv.imread('Photo/odst_classic.jpg')
    resized_image = rescaleFrame(img)
    cv.imshow('ODST', img)
    cv.imshow('rODST', resized_image)

    cv.waitKey(0)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
