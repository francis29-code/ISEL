<?php

require_once( "../Lib/lib.php" );

$operation = $_POST['operation'];

$name = webAppName();

header(
        "Location: " .
        $name . "formManageAccounts" . $operation . ".php");
?>
