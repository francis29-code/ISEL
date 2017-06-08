<?php

require_once( "../Lib/lib.php" );
require_once( "../Lib/db.php" );
require_once( "../Lib/lib-coords.php" );
require_once( "../Lib/ImageResize-class.php" );

include_once( "config.php" );

header('Content-Type: text/html; charset=utf-8');

// Maximum time allowed for the upload
set_time_limit(300);

if ($_FILES['userFile']['error'] != 0) {
    // Handle the error
    $errorCode = $_FILES['userFile']['error'];

    echo showUploadFileError($errorCode);

    exit($errorCode);
}

// Original name of the file that was uploaded
$srcName = $_FILES['userFile']['name'];

if (($srcName <> "none") && ($srcName <> "" )) {
    // We have a file
    // Read configurations from data base
    $configurations = getConfiguration();
    $dstDir = $configurations['destination'];

    // Destination for the uploaded file
    $src = $_FILES['userFile']['tmp_name'];
    $dst = $dstDir . DIRECTORY_SEPARATOR . $srcName;

    if (copy($src, $dst)) {
        unlink($src);

        echo "File uploaded with sucess.\n<br>";

        $fileInfo = finfo_open(FILEINFO_MIME);

        $fileInfoData = finfo_file($fileInfo, $dst);
        print_r($fileInfoData);

        $fileTypeComponents = explode(";", $fileInfoData);

        $mimeTypeFileUploaded = explode("/", $fileTypeComponents[0]);
        $mimeFileName = $mimeTypeFileUploaded[0];
        $typeFileName = $mimeTypeFileUploaded[1];

        $thumbsDir = $dstDir . DIRECTORY_SEPARATOR . "thumbs";
        $pathParts = pathinfo($dst);

        $lat = "";
        $lon = "";

        if ($_POST['description'] != NULL) {
            $description = addslashes($_POST['description']);
        } else {
            $description = "No description available";
        }

        if ($_POST['title'] != NULL) {
            $title = addslashes($_POST['title']);
        } else {
            $pathParts = pathinfo($srcName);
            $title = $pathParts['filename'];
        }

        $width = $configurations['thumbWidth'];
        $height = $configurations['thumbHeight'];

        echo "File is of type $mimeFileName<br>\n";

        $imageFileNameAux = null;
        $imageMimeFileName = null;
        $imageTypeFileName = null;

        $thumbFileNameAux = null;
        $thumbMimeFileName = null;
        $thumbTypeFileName = null;

        switch ($mimeFileName) {
            case "image":
                $exif = @exif_read_data($dst, 'IFD0', true);
                if ($exif === false) {
                    echo "No exif header data found.<br>\n";
                } else {
                    //Just for Debug - Begin
//            echo "<pre>";
//            echo "<pre>";
//            foreach ($exif as $key => $section) {
//              foreach ($section as $name => $val) {
//                echo "$key.$name: $val<br>\n";
//              }
//            }
                    //Just for Debug - End

                    $gps = $exif['GPS'];
                    if ($gps != NULL) {
                        $latitudeAux = $gps['GPSLatitude'];
                        $latitudeRef = $gps['GPSLatitudeRef'];
                        $longitudeAux = $gps['GPSLongitude'];
                        $longitudeRef = $gps['GPSLongitudeRef'];

                        if (($latitudeAux != NULL) && ($longitudeAux != NULL)) {
                            $lat = getCoordAsString($latitudeAux, $latitudeRef);
                            $lon = getCoordAsString($longitudeAux, $longitudeRef);
                            echo "File latitude: $lat<br>\n";
                            echo "File longitued: $lon<br>\n";
                        } else {
                            echo "File does have GPS coordenates<br>\n";
                        }
                    } else {
                        echo "File does have GPS coordenates<br>\n";
                    }
                }

                $imageFileNameAux = $dst;
                $imageMimeFileName = "image";
                $imageTypeFileName = $typeFileName;

                $thumbFileNameAux = $thumbsDir . DIRECTORY_SEPARATOR . $pathParts['filename'] . "." . $typeFileName;
                $thumbMimeFileName = "image";
                $thumbTypeFileName = $typeFileName;

                $resizeObj = new ImageResize($dst);
                $resizeObj->resizeImage($width, $height, 'crop');
                $resizeObj->saveImage($thumbFileNameAux, $typeFileName, 100);
                $resizeObj->close();
                break;

            case "video":
                $size = "$width" . "x" . "$height";

                $imageFileNameAux = $thumbsDir . DIRECTORY_SEPARATOR . $pathParts['filename'] . "-Large.jpg";
                $imageMimeFileName = "image";
                $imageTypeFileName = "jpeg";
                echo "Generating video 1st image...<br>\n";

                $cmdFirstImage = " $ffmpegBinary -itsoffset -1  -i $dst -vcodec " .
                        "mjpeg -vframes 1 -an -f rawvideo -s 640x480 $imageFileNameAux";

                echo "$cmdFirstImage<br>\n";
                system($cmdFirstImage, $status);
                echo "Status from the generation of video 1st image: $status.<br>\n";

                $thumbFileNameAux = $thumbsDir . DIRECTORY_SEPARATOR . $pathParts['filename'] . ".jpg";
                $thumbMimeFileName = "image";
                $thumbTypeFileName = "jpeg";
                echo "Generating video thumb...<br>\n";
                $cmdVideoThumb = "$ffmpegBinary -itsoffset -5  -i $dst -vcodec mjpeg -vframes 1 -an -f rawvideo -s $size $thumbFileNameAux";
                echo "$cmdVideoThumb<br>\n";
                system($cmdVideoThumb, $status);
                echo "Status from the generation of video thumb: $status.<br>\n";
                break;

            case "audio":
                require_once( "Zend/Media/Id3v2.php" );

                $id3 = new Zend_Media_Id3v2($dst);

                $mimeTypeAudioAPIC = explode("/", $id3->apic->mimeType);
                //$mimeAudioAPIC = $mimeTypeAudioAPIC[0];
                $typeAudioAPIC = $mimeTypeAudioAPIC[1];

                $imageFileNameAux = $thumbsDir . DIRECTORY_SEPARATOR . $pathParts['filename'] . "-Large." . $typeAudioAPIC;
                $imageMimeFileName = "image";
                $imageTypeFileName = $typeAudioAPIC;
                $fdMusicImage = fopen($imageFileNameAux, "wb");
                fwrite($fdMusicImage, $id3->apic->getImageData());
                fclose($fdMusicImage);

                $thumbFileNameAux = $thumbsDir . DIRECTORY_SEPARATOR . $pathParts['filename'] . "." . $typeAudioAPIC;
                $thumbMimeFileName = "image";
                $thumbTypeFileName = $typeAudioAPIC;
                $resizeObj = new ImageResize($imageFileNameAux);
                $resizeObj->resizeImage($width, $height, 'crop');
                $resizeObj->saveImage($thumbFileNameAux, $typeAudioAPIC, 100);
                $resizeObj->close();
                break;

            default:
                $imageFileNameAux = $dstDir . DIRECTORY_SEPARATOR . "default" . DIRECTORY_SEPARATOR . "Unknown-Large.jpg";
                $imageMimeFileName = "image";
                $imageTypeFileName = "jpeg";

                $thumbFileNameAux = $dstDir . DIRECTORY_SEPARATOR . "default" . DIRECTORY_SEPARATOR . "Unknown.jpg";
                $thumbMimeFileName = "image";
                $thumbTypeFileName = "jpeg";
                break;
        }

        // Write information about file into the data base
        dbConnect(ConfigFile);
        mysqli_select_db($GLOBALS['ligacao'], $GLOBALS['configDataBase']->db);

        $latitude = addslashes($lat);
        $longitude = addslashes($lon);

        $fileName = addslashes($dst);
        $imageFileName = addslashes($imageFileNameAux);
        $thumbFileName = addslashes($thumbFileNameAux);

        $query = "INSERT INTO `images-details`" .
                "(`fileName`, `mimeFileName`, `typeFileName`, `imageFileName`, `imageMimeFileName`, `imageTypeFileName`, `thumbFileName`, `thumbMimeFileName`, `thumbTypeFileName`, `latitude`, `longitude`, `title`, `description`) values " .
                "('$fileName', '$mimeFileName', '$typeFileName', '$imageFileName', '$imageMimeFileName', '$imageTypeFileName', '$thumbFileName', '$thumbMimeFileName', '$thumbTypeFileName', '$latitude', '$longitude', '$title', '$description')";

        mysqli_query($GLOBALS['ligacao'], $query);

        $recordsInserted = mysqli_affected_rows($GLOBALS['ligacao']);

        if ($recordsInserted == -1) {
            echo "Information about file could not be insert into the data base.\n<br>";
        } else {
            echo "Information about file was insert into data base.\n<br>";
        }

        dbDisconnect();

        echo "<a href='javascript:history.back()'>Back</a>";
    } else {
        echo "Could not write file to $dst";
    }
} else {
    echo "File not specified.<br>";
}
?>