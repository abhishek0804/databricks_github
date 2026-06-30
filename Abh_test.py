# Databricks notebook source
print('hello new version')
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--catalog")
parser.add_argument("--schema")

args = parser.parse_args()

print(args.catalog)
print(args.schema)