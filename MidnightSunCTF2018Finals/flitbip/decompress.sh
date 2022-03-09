#!/bin/sh

mkdir rootfs
cd rootfs
cp ../initrd ./initrd.gz
gunzip ./initrd.gz
cpio -idm < ./initrd
rm initrd
