<?php

require_once( "../../Lib/lib.php" );
require_once( "../../Lib/db.php" );

$name = webAppName();

$url = $name . "index.php";

ensureAuth($url);

include( "header.php" );

echo "Resource2";

include( "menu2.php" );
?>