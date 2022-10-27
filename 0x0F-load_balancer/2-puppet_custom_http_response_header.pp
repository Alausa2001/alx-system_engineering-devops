# creating a custom HTTP header response, but with Puppet

exec {'update':
  command  => 'sudo apt-get -y update',
  provider => 'shell',
  before   => Package['nginx']
}

package {'nginx':
  ensure => 'installed',
  before => Exec['customheader']
}
$host = $hostname
exec {'customheader':
  command  => "sudo sed -e '52i \\\t\tadd_header X-Served-By ${host};' -i /etc/nginx/sites-available/default;",
  provider => 'shell',
  before   => Exec['restart']
}

exec {'restart':
  user     => root,
  command  => 'sudo service nginx restart',
  provider => 'shell'
}
