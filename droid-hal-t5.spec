# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device t5
%define vendor fxtec

%define vendor_pretty F(x)tec
%define device_pretty Pro1

%define installable_zip 1
%define droid_target_aarch64 1

# want adreno quirks is required for browser at least, and other subtle issues
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define makefstab_skip_entries /mnt/vendor/persist /dev/cpuctl /dev/stune /sys/fs/bpf

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

