<html lang="en">
<head>
    <meta charset="utf-8"/>
    <title>AliBestOf</title>
    <meta name="description" content=""/>
    <meta name="keywords" content=""/>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
    <meta name="author" content="Piotr Bartoszewski">
    <meta name="viewport" content="width=device-width"/>
    <link rel="stylesheet" href="css/style.css" type="text/css">
    <link href="img/icons/icon.png" rel="shortcut icon">
	<link href="https://fonts.googleapis.com/css?family=Nunito|Open+Sans&display=swap" rel="stylesheet">
</head>

<script>
    document.addEventListener('contextmenu', event => event.preventDefault());
</script>

<body>
<header>
    <a class="title" href="index.php"> AliBestOf </a>

    <form action="search.php" method="get">
        <div class="search">
            <input type="text" name="query" placeholder="Search for products..."/>
            <button type="submit">&#x1F50D</button>
        </div>
        <div class="clearBoth"></div>
    </form>
</header>

<article>
    <?php
    $itemsPerPage = 40;

    if (isset($_GET["page"]) && !empty($_GET["page"]))
        $currentPage = $_GET["page"];
    else
        $currentPage = 1;

    $start = ($currentPage - 1) * $itemsPerPage;
    $limit = $itemsPerPage;

    require_once "dbConnect.php";

    if ($result = @$connection->query("SELECT * FROM $table_products WHERE hidden=0 ORDER BY id DESC LIMIT {$start}, {$limit} ")) {
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
    } else {
        echo "No such table '$table_products' found in the database";
        exit();
    }

    $totalItems = @$connection->query("SELECT * FROM $table_products WHERE hidden=0")->num_rows;
    $totalPages = ceil($totalItems / $itemsPerPage);


    if($totalPages > 1) {
        echo '<br/><br/>';
        for ($i = 1; $i <= $totalPages; $i++) {
            echo <<< _END
    <a href="index.php?page=$i">
        <button>$i</button>
    </a>
_END;
        }
    }
    ?>
</article>

<footer>
    <label>&copy AliBestOf All Rights Reserved!</label>
</footer>
</body>
</html>