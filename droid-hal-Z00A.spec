%define device Z00A
%define vendor asus

%define vendor_pretty ASUS
%define device_pretty Zenfone 2

%define installable_zip 1
%define device_target_cpu i486 

%define straggler_files \
/intel_prop.cfg \
%{nil}

%include rpm/dhd/droid-hal-device.inc
