# configure nginx

exec { 'update':
  command => 'sudo apt-get -y upgrade'
}

package { 'nginx':
  ensure   => 'installed',
  provider => 'apt'
}

file { 'index.html':
  path    => '/var/www/html/index.html',
  owner   => 'root',
  comtent => 'Hello world'
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.github.com/Alausa2001 permanent';
}
