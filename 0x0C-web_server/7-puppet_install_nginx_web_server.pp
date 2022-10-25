# configure nginx

exec {'update':
  command => 'sudo apt-get -y update',
  path    => '/usr/bin/'
}

package {'nginx':
  ensure   => 'installed'
}

file {'index.html':
  path    => '/var/www/html/index.html',
  owner   => 'root',
  content => 'Hello World!'
}

file_line {'redirect':
  ensure            => 'present',
  path              => '/etc/nginx/sites-available/default',
  line              => 'rewrite ^/redirect_me https://www.github.com/Alausa2001 permanent;',
  match_for_absence => 'true'
}
