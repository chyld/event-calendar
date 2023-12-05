#!/bin/bash

rm database.sqlite
sqlite3 database.sqlite < schema.sql
sqlite3 database.sqlite '.schema'
