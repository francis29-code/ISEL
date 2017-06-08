<?php

if($_POST){
  require_once("../lib/db.php");

  $username = $_POST['username'];
  $password = $_POST['password'];

  dbConnect(credenciaisDB);

  mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);

  $query = "SELECT * FROM `userclient` WHERE username='$username' and password='$password'";

  $result = mysqli_query($GLOBALS['ligacao'], $query);

  if(mysqli_num_rows($result)==1){
    session_start();
    $_SESSION['auth'] = 'true';
  }else{

    // echo "<a>wrong credencials</a>";
  }
  dbDisconnect();
}

?>

<div class="container">
  <div class="row">
    <!-- col-md-offset posiciona dentro da div-->
    <div class="col-md-4 col-md-offset-4">
      <form class="form-horizontal" method="GET" onsubmit="ajax('otherpages/registo.php',loadRegisto,'GET')">
        <div class="form-group">
          <label class="control-label col-sm-2" for="email">Username:</label>
          <div class="col-sm-10">
            <input type="text" class="form-control" name="username" placeholder="Enter username">
          </div>
        </div>
        <div class="form-group">
          <label class="control-label col-sm-2" for="pwd">Password:</label>
          <div class="col-sm-10">
            <input type="password" class="form-control" name="password" placeholder="Enter password">
          </div>
        </div>
        <div class="form-group">
          <div class="col-sm-offset-2 col-sm-10">
            <input type="submit" class="btn btn-default"></input>
          </div>
        </div>
      </form>
    </div>
  </div>
</div>
