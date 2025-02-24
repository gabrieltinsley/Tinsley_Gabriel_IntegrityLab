#!/bin/bash
# Prevent execution of untrusted scripts
chmod 700 /trusted_apps/*
setfacl -m u:untrusted_user:--x /trusted_apps/*