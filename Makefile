# Makefile for source rpm: gd
# $Id$
NAME := gd
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
