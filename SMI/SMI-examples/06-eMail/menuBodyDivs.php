<?php
require_once '../Lib/lib.php';

$name = webAppName();
?>  

<a id="linkFormManageAccounts" href="#" onclick="getContent('formManageAccountsBody.php');return false;">Manage e-mail accounts</a>
<br>

<a id="linkFormManageContacts" href="#" onclick="getContent('formManageContactsBody.php');return false;">Manage e-mail contacts</a>
<br>

<a id="linkFormSend" href="#" onclick="getContent('formSendBody.php');return false;">Send e-mail</a>
<br>

<a id="linkFormSendHTML" href="#" onclick="getContent('formSendHTMLBody.php');return false;">Send HTML e-mail</a>
<br>

<a id="linkFormSendHTML" href="#" onclick="getContent('formSendPHPBody.php');return false;">Send e-mail using PHP</a>
<br>

<a id="linkLinks" href="#" onclick="getContent('linksBody.php');return false;">Useful links</a>
<br>

<a target="_top" href="index.html">Back to e-mail Examples</a>
<br>
