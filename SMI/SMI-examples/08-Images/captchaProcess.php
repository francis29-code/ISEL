<?php

session_start();

header('Content-Type: text/html; charset=utf-8');

if ($_SESSION['captcha'] == $_POST['captcha']) {
    echo "<h1>Ok - Code is correct</h1>";
} else {
    echo "<h1>Error - Code is incorrect</h1>";
}
?>