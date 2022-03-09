#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/sched.h>
#include <linux/syscalls.h>

#define MAXFLIT 1

#ifndef __NR_FLITBIP
#define FLITBIP 333
#endif

long flit_count = 0;
EXPORT_SYMBOL(flit_count);

SYSCALL_DEFINE2(flitbip, long *, addr, long, bit)
{
        if (flit_count >= MAXFLIT)
        {
                printk(KERN_INFO "flitbip: sorry :/\n");
                return -EPERM;
        }

        *addr ^= (1ULL << (bit));
        flit_count++;

        return 0;
}
