<?php
if (!isset($_GET['productName']) || empty($_GET['productName'])) {
    header('Location: index.php');
}

require_once "dbConnect.php";
$sql = "SELECT * FROM $table_products WHERE hidden=0 AND name='{$_GET['productName']}'";

if ($result = $connection->query($sql)) {
    if (($result->num_rows) == 0) {
        header("Location: index.php");
    }
}
?>

<html lang="en">
    <head>
        <meta charset="utf-8"/>
        <title>AliBestOf - Product Info</title>
        <meta name="description" content=""/>
        <meta name="keywords" content=""/>
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
        <meta name="author" content="Piotr Bartoszewski">
        <meta name="viewport" content="width=device-width"/>
        <link rel="stylesheet" href="css/style.css" type="text/css">
        <link href="img/icons/icon.png" rel="shortcut icon">
        <link href="https://fonts.googleapis.com/css?family=Nunito|Open+Sans&display=swap" rel="stylesheet">

        <script>
            window.ao_subid = "";
        </script>
        <script src="//js.mamydirect.com/js/?h=kJlyQUb9" type="text/javascript" async></script>

        <script>
            document.addEventListener('contextmenu', event => event.preventDefault());
        </script>
    </head>

    <body>
        <header>
            <a class="title" href="index.php"> AliBestOf </a>
        </header>

        <article id="productInfo">
            <?php

            if ($result = $connection->query("SELECT * FROM $table_products WHERE hidden=0 AND name='{$_GET['productName']}'")) {
                $product = $result->fetch_assoc();

                $imgPath = "img/products/{$product['name']}";

                if (file_exists($imgPath . ".png"))
                    $imgPath = $imgPath . ".png";
                else if (file_exists($imgPath . ".jpg"))
                    $imgPath = $imgPath . ".jpg";
                else if (file_exists($imgPath . ".jpeg"))
                    $imgPath = $imgPath . ".jpeg";
                else if (file_exists($imgPath . ".gif"))
                    $imgPath = $imgPath . ".gif";

                echo <<< _END
    <div class="productInfo">
        <img src="{$imgPath}"/>

        <span>
                <strong>Name:</strong>
                {$product['name']}

                <br/><br/>
                <strong>Description:</strong>
                {$product['description']}

                <br/><br/>
                <form action="{$product['reflink']}">
                    <button type="submit" >LINK</button>
                </form>
        </span>
    </div>
    <iframe src="{$product['link']}" align="center" width="100%" height="60%" frameborder="0"></iframe>
_END;
            } else {
                echo <<< _END

<label>Error: $connection->connect_errno</label>

_END;
                exit();
            }
            ?>
        </article>
    </body>
</html>