#fix extension from "phpp" to "php"

exec{'fix-extension':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/user/local/bin/:/bin/'
}
