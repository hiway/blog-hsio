Title: Linux on Thinkpad x280 intermittently freezes [solved]
Date: 2023-07-03
Category: Linux

It appears that the random intermittent freezes every few minutes 
where the desktop/apps/pointer is unresponsive for a second or more
is not limited to Fedora or Thinkpad.

The reason is likely Intel i915 GPU.

I [found a discussion on Reddit](https://www.reddit.com/r/thinkpad/comments/rhbf8m/solution_thinkpad_short_freezes_on_gnulinux/) that documents a solution in parts
spread out over several comments for the complete answer:



Documenting the steps/files below for next time I'm in the same situation.

Edit `/etc/default/grub`:

```diff
5a6
> GRUB_CMDLINE_LINUX_DEFAULT="i915.enable_psr=0 psmouse.synaptics_intertouch=1"
8c9
< GRUB_ENABLE_BLSCFG=true
---
> GRUB_ENABLE_BLSCFG=false
```

- `i915.enable_psr=0` to resolve the hangs
- `psmouse.synaptics_intertouch=1` to improve touchpad functionality
- `GRUB_ENABLE_BLSCFG=false` to ensure Fedora boots up

Run the following commands to update grub config and reboot
```
sudo mv /boot/grub2/grub.cfg /root/boot-grub2-grub.cfg.bak
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
sudo reboot
```

Have not encountered any freezes for over 24 hours now.
