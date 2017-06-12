<?php

require_once ('./getEmailConfig.php');
require_once( "../Lib/db.php");
require_once( "../Lib/lib.php");
require_once( "../Lib/lib-mail-v2.php" );


getEmailConfigurations();

$timeout = 100;

$dominio_src = getEmailDomain($username);

dbConnect(ConfigFile);
mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);

$query = "Select * from email where dominio ='" . $dominio_src . "'";
$result = mysqli_query($GLOBALS['ligacao'], $query);
$dominio_info = mysqli_fetch_array($result);

$dominio_src = $dominio_info['dominio'];
$smtp_server = $dominio_info['smtp_server'];
$port = $dominio_info['port'];
$UseSsl = $dominio_info['UseSsl'];
mysqli_free_result($result);
$fromEmail = $username;
$username = "roloisel20"; //username escolhido pelo user
$fromName = "Fábio Rolo"; //nome + apelido do user
$toList = "fabio_miguel12@hotmail.com";
$subject = "Ola Rolo";
$nome_server = $_SERVER['SERVER_NAME'];
$server_port = 80;
$message = "Carregue no seguinte link para completar a sua inscrição" . " http://" . $nome_server . ":" . $server_port . "/smi1617/01-Hello/index.php?user=" . $username;
/*
  print_r("SMTP SERVER : ".$smtp_server . " \n");
  print_r("ssl: ". $UseSsl . " \n");
  print_r("port: ".$port . " \n");
  print_r("timeout: ".$timeout . " \n");
  print_r("username: ".$username . " \n");
  print_r("password: ". $password . " \n");
  print_r("do mail: ".$fromEmail . " \n");
  print_r("do nome: ".$fromName . " \n");
  print_r("mails: ". $toList . " \n");
  print_r("conteudo: ".$subject . " \n");
  print_r("mensagem: ".$message . " \n");
 */

$result = sendAuthEmail($smtp_server, $UseSsl, $port, $timeout, $username, $password, $fromEmail, $fromName, $toList, NULL, NULL, $subject, $message, NULL);

if ($result == TRUE) {
    echo "<script>alert('E-mail was delivered to e-mail server.')</script>";
} else {
    echo "<script>alert('E-mail couldn't be delivered to e-mail server.')</script>";
}

dbDisconnect();
?>
