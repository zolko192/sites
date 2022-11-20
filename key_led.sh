xset q | awk '/LED/{ if ($10 ~ "00000002") print "led"; else print "-led" }' | xargs xset
