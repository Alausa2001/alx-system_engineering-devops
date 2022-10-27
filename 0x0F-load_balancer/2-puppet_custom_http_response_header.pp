# install haproxy and configure it to distribute traffic between two servers using roundrobin algorithm
exec { 'update':
  command  => 'sudo apt-get -y update',
  provider => 'shell'
}

package { 'haproxy':
  ensure => 'installed'
}

exec { 'frontend':
  command  => 'sudo sed -e "34a frontend http\n\tbind *:80\n\tmode http\n\tdefault_backend feranmi_backend" -i /etc/haproxy/haproxy.cfg',
  provider => 'shell'
}
$bckend = 'backend feranmi_backend\n\tbalance roundrobin\n\tserver 34482-web-01 18.204.227.153:80 check'
exec {'backend':
  command  => "sudo sed -e '38a ${bckend}' -i /etc/haproxy/haproxy.cfg",
  provider => 'shell'
}

exec {'backend2':
  command  => "sudo sed -e '41a \\\tserver 34482-web-02 34.232.53.153:80 check' -i /etc/haproxy/haproxy.cfg",
  provider => 'shell'
}

exec {'service':
  command  => 'sudo service haproxy restart',
  provider => 'shell'
}
