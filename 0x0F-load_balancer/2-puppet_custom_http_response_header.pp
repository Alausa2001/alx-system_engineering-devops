# creating a custom HTTP header response, but with Puppet

exec {'update':
  command  => 'sudo apt-get -y update',
  provider => 'shell'
}

package {'nginx':
  ensure => 'installed'
}

exec {'customheader':
  command  => "sudo sed -e '52i \\\t\tadd_header X-Served-By ${hostname};' -i /etc/nginx/sites-available/default;",
  provider => 'shell'
}

exec {'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell'
}
