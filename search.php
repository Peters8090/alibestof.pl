<?php
if (!isset($_GET['query']) || empty($_GET['query'])) {
    header("Location: index.php");
    exit();
}
?>

<html lang="en">
    <head>
        <meta charset="utf-8"/>
        <title>AliBestOf - Search</title>
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

        <article>
            <?php
            require_once "dbConnect.php";

            $_GET['query'] = htmlentities($_GET['query'], ENT_QUOTES, "UTF-8");
            $_GET['query'] = mysqli_real_escape_string($connection, $_GET['query']);

            if ($result = $connection->query("SELECT * FROM $table_products WHERE hidden=0 AND (id='{$_GET['query']}' OR (name LIKE '%{$_GET['query']}%')  OR (description LIKE '%{$_GET['query']}%')) ORDER BY id DESC")) {
                if (($result->num_rows) == 0) {
                    echo <<< _END
    <br/>
    <label>Not found</label>
_END;
                    exit();
                } else {
                    foreach ($result as $product) {
                        $imgPath = "img/products/{$product['name']}";

                        if(file_exists($imgPath.".png"))
                            $imgPath = $imgPath.".png";
                        else if(file_exists($imgPath.".jpg"))
                            $imgPath = $imgPath.".jpg";
                        else if(file_exists($imgPath.".jpeg"))
                            $imgPath = $imgPath.".jpeg";
                        else if(file_exists($imgPath.".gif"))
                            $imgPath = $imgPath.".gif";

                        echo <<< _END
    <form action="productInfo.php" method="GET"
        <div class='product'>
            <img src="{$imgPath}"/>
            <input type="text" name="productName" readonly="readonly" value="{$product['name']}"/>
            <button type="submit" >MORE</button>
        </div>
    </form>
_END;
                    }
                }
            } else {
                echo <<< _END

<label>Error: $connection->connect_errno</label>

_END;
            }
            ?>
        </article>
    </body>
</html>