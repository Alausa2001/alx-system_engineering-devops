#!/usr/bin/env ruby
puts ARGV[0].scan(/from:([A-Za-z0-9+]+)\]\s\[to:([+\w]+)\]\s\[flags:([-:\d]+)/).join(',')
