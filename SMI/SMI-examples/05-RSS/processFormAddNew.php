<!DOCTYPE html>
<?php
header('Content-Type: text/html; charset=utf-8');

$_description = $_POST['description'];
$_author = $_POST['author'];
$_title = $_POST['title'];
$_contents = $_POST['contents'];

$ServerName = $_SERVER['SERVER_NAME'];
$ServerPort = $_SERVER['SERVER_PORT'];

require_once( "../Lib/db.php" );
require_once( "../Lib/lib.php" );

$description = addslashes($_description);
$author = addslashes($_author);
$title = addslashes($_title);
$contents = addslashes($_contents);

$name = webAppName();

dbConnect(ConfigFile);

$db = $GLOBALS['configDataBase']->db;

mysqli_select_db($GLOBALS['ligacao'], $db);

$queryInsertNew = "INSERT INTO `smi`.`rss-news`" .
        "(`description`, `author`, `link`, `title`, `contents`, `pubDate`) values " .
        "('$description', '$author', '', '$title', '$contents', CURDATE() )";

echo "Description:\n<br>$description\n<br>";
echo "Author:\n<br>$author\n<br>";
echo "Link:\n<br>http://" .
 $ServerName . ":" . $ServerPort .
 $name . "getRSS.php?idNew=...\n<br>";
echo "Title:\n<br>$title\n<br>";
echo "Contents:\n<br>$contents\n<br>";
echo "SQL statment:\n<br>$queryInsertNew\n<br>";

mysqli_query($GLOBALS['ligacao'], $queryInsertNew);

$recordsInserted = mysqli_affected_rows($GLOBALS['ligacao']);

if ($recordsInserted == -1) {
    echo "Insert of RSS has failed!";
} else {
    echo "RSS added with success.";
}

dbDisconnect();
?>