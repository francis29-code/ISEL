<?php

include_once( "config.php" );
include_once( "configDebug.php" );

session_start();

include_once( "configDebug.php" );

$_SESSION['captcha'] = $captchaValue;

$imageCaptcha = ImageCreateFromPNG("images/fundocaptch.png");

$colorCaptcha = imagecolorallocate($imageCaptcha, 255, 0, 0);

$fontName = "Vera.ttf";
//$fontName = "VeraBd.ttf";
//$fontName = "VeraBI.ttf";
//$fontName = "VeraIt.ttf";
//$fontName = "VeraMoBd.ttf";
//$fontName = "VeraMoBI.ttf";
//$fontName = "VeraMoIt.ttf";
//$fontName = "VeraMono.ttf";
//$fontName = "VeraSe.ttf";
//$fontName = "VeraSeBd.ttf";

$fontCaptcha = $fontsDirectory . $fontName;

$code1 = substr($captchaValue, 0, 4);
$code2 = substr($captchaValue, 4, 9);

//  imagettftext(
//    $imageCaptcha,    // Image
//    20,               // Font size
//    -5,                // Font angle
//    40,               // X position
//    30,               // Y position
//    $colorCaptcha,    // Font color
//    $fontCaptcha,     // Font type
//    $codeCaptcha      // Text to write
//    );

imagettftext(
        $imageCaptcha, // Image
        20, // Font size
        -5, // Font angle
        40, // X position
        30, // Y position
        $colorCaptcha, // Font color
        $fontCaptcha, // Font type
        $code1              // Text to write
);

imagettftext(
        $imageCaptcha, // Image
        20, // Font size
        5, // Font angle
        120, // X position
        30, // Y position
        $colorCaptcha, // Font color
        $fontCaptcha, // Font type
        $code2              // Text to write
);

/*
  $fontCaptcha = 4;

  imagestring(
  $imageCaptcha,
  $fontCaptcha,
  15,
  15,
  $codeCaptcha,
  $corCaptcha);
 */


header("Content-type: image/png");

imagepng($imageCaptcha);

imagedestroy($imageCaptcha);
?>