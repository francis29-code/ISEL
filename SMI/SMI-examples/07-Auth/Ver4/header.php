<?php
@session_start();

//  if ( !isset($_SESSION) ) {
//    session_start();
//  }

if (isset($_SESSION['username'])) {
    require_once( "../../Lib/lib.php" );
    require_once( "../../Lib/db.php" );

    $user = $_SESSION['username'];
    $id = $_SESSION['id'];
    $userRole = getRole($id);

    echo "<div style=\"font-weight:bold;text-align:right\">$user, $userRole</div>";
}
?>
<hr>