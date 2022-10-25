# configure nginx

exec { 'update':
  command => 'sudo apt-get -y upgrade'
}

exec { 'nginx':
  command   => 'sudo apt-get -y install nginx'
}

file { 'index.html':
  path    => '/var/www/html/index.html',
  owner   => 'root',
  comtent => 'Hello World!'
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.github.com/Alausa2001 permanent';
}
