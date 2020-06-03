<!DOCTYPE html>
<html>
<head>
	<title>Récupération de données</title>
	<meta charset="utf-8">

	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

<body>
	<h1 class="text-center">Récupération de données footbalistique</h1>
	<br/><br/>
	</body>
	<h4 class="text-center">Veuillez choisir le type de données que vous voulez</h4>
	<form method="GET">

		<div class="text-center">
		<!-- Material inline 1 -->
		<div class="form-check form-check-inline">
		  <input type="radio" class="form-check-input" id="Joueur" name="choixAPI" value="0" onchange="this.form.submit()">
		  <label class="form-check-label" for="materialInline1">Joueur</label>
		</div>

		<!-- Material inline 2 -->
		<div class="form-check form-check-inline">
		  <input type="radio" class="form-check-input" id="League" name="choixAPI" value="1" onchange="this.form.submit()">
		  <label class="form-check-label" for="materialInline2">League</label>
		</div>

		<!-- Material inline 3 -->
		<div class="form-check form-check-inline">
		  <input type="radio" class="form-check-input" id="Match" name="choixAPI" value="2" onchange="this.form.submit()">
		  <label class="form-check-label" for="materialInline3">Match</label>
		</div>

		<!-- Material inline 4 -->
		<div class="form-check form-check-inline">
		  <input type="radio" class="form-check-input" id="Equipe" name="choixAPI" value="3" onchange="this.form.submit()">
		  <label class="form-check-label" for="materialInline4">Equipe</label>
		</div>

		<!-- Material inline 5 -->
		<div class="form-check form-check-inline">
		  <input type="radio" class="form-check-input" id="Transfer" name="choixAPI" value="4"  onchange="this.form.submit()">
		  <label class="form-check-label" for="materialInline5">Transfer</label>
		</div>
		</div>
		

	</form>

		<?php
		if(isset($_GET["choixAPI"])){
			if($_GET["choixAPI"] == 0){?>
			<br/>
			<hr color="black">
			<form method="POST">
				<div class="text-center">
				<!-- Material inline 1 -->
				<div class="form-check form-check-inline">
				  <input type="radio" class="form-check-input" id="Joueur" name="typeP" value="0" onchange="this.form.submit()">
				  <label class="form-check-label" for="materialInline1">Recheche de l'ensemble des joueurs d'une équipe</label>
				</div>

				<!-- Material inline 2 -->
				<div class="form-check form-check-inline">
				  <input type="radio" class="form-check-input" id="League" name="typeP" value="1" onchange="this.form.submit()">
				  <label class="form-check-label" for="materialInline2">Recherche de données sur un joueur</label>
				</div>
				</div>

			</form>


<!-- <?php ?> -->


			<?php 
			if(isset($_POST["typeP"])){
			if($_POST["typeP"] == 0){
			?>
			
			<hr color="black">
			<br/>
			<div class="container">
			<div class="basic_form">
				<form method="POST" action="Recherche.php">
			
					<div class="text-center">
						<label  for='pays'>Pays :</label></br>
						<input class='form-control' type='text' name='pays' id='pays' placeholder='Veuillez entrer le nom du pays'/></br>
				  	</div>

				  	<div class="text-center">
						<label for='club'>Nom du club :</label></br>
						<input class='form-control' type='text' name='club' id='club' placeholder="Veuillez entrer le nom de l'équipe" /></br>
				  	</div>


				  	<div class="modal-footer">
						<button class="btn btn-primary" name="valPlayer" type="submit" value="Valider">Valider</button>
					</div>

			    </form>
		    </div>
			</div>
		  <?php }



		  elseif ($_POST["typeP"]==1) {
		  	
		  ?>
			<hr color="black">
			<br/>
			<div class="container">
			<div class="basic_form">
				<form method="POST" action="Recherche.php">
				  	<div class="text-center">
						<label for='fn'>Prénom :</label></br>
						<input class='form-control' type='text' name='fn' id='fn' placeholder='Veuillez entrer le prénom du joueur'/></br>
				  	</div>
				  	<div class="text-center">
						<label for='ln'>Nom :</label></br>
						<input class='form-control' type='text' name='ln' id='ln' placeholder='Veuillez entrer le nom du joueur'/></br>
				  	</div>

					<div class="text-center">
					<div class="form-check form-check-inline">
					  <input type="radio" class="form-check-input" id="pm" name="dataP" value="0">
					  <label class="form-check-label" for="0">Tous les matchs du joueur</label>
					</div>

					<div class="form-check form-check-inline">
					  <input type="radio" class="form-check-input" id="pi" name="dataP" value="1" >
					  <label class="form-check-label" for="1">Inforamtion sur le joueur</label>
					</div>


					<div class="form-check form-check-inline">
					  <input type="radio" class="form-check-input" id="pc" name="dataP" value="2">
					  <label class="form-check-label" for="2">La carière du joueur</label>
					</div>


					<div class="form-check form-check-inline">
					  <input type="radio" class="form-check-input" id="all" name="dataP" value="3" >
					  <label class="form-check-label" for="3">Toutes les informations disponibles</label>
					</div>
					</div>



					<br/><br/>
				  	<div class="modal-footer">
						<button class="btn btn-primary" name="valPlayerJ" type="submit" value="Valider">Valider</button>
					</div>

					</div>
	 	</form>
			</div>
			</div>
<?php
					}
				}
			}
// --------------------------------- Fin des formulaire joueurs ----------------------------------------------


// --------------------------------- Début formulaire league --------------------------------------

	if($_GET["choixAPI"] == 1){?>
				
			<br/>
			<hr color="black">
			<form method="POST">
				<div class="text-center">

				<div class="form-check form-check-inline">
				  <input type="radio" class="form-check-input" id="Joueur" name="typeL" value="0" onchange="this.form.submit()">
				  <label class="form-check-label" for="materialInline1">Ensemble des ligues d’un pays</label>
				</div>

				<div class="form-check form-check-inline">
				  <input type="radio" class="form-check-input" id="League" name="typeL" value="1" onchange="this.form.submit()">
				  <label class="form-check-label" for="materialInline2">Ensemble des ligues d’un pays et de leurs types</label>
				</div>

				<div class="form-check form-check-inline">
				  <input type="radio" class="form-check-input" id="League" name="typeL" value="2" onchange="this.form.submit()">
				  <label class="form-check-label" for="materialInline2">Ensemble des ligues d’un pays et des sous-divisions qu’elle peuvent avoir </label>
				</div>

				<div class="form-check form-check-inline">
				  <input type="radio" class="form-check-input" id="League" name="typeL" value="3" onchange="this.form.submit()">
				  <label class="form-check-label" for="materialInline2">L’équipe gagnante ou l’ensemble des équipes gagnantes</label>
				</div>
			</div>
			</form>
<?php 
if(isset($_POST["typeL"])){
	if($_POST["typeL"] == 0){?>
		<br/> <hr color="black">
		<form method="POST" action="Recherche.php?choixAPI=1">
		<div class="container">

			<div class="text-center">
				<label for='fn'>Nom du pays :</label></br>
				<input class='form-control' type='text' name='Lpays1' id='Lpays1' placeholder='Veuillez entrer le nom du pays'/></br>
			</div>

			<br/><br/>
				<div class="modal-footer">
					<button class="btn btn-primary" name="league1" type="submit" value="Valider">Valider</button>
			</div>
			</div>
		</form>

<?php
	}
	if($_POST["typeL"] == 1){?>
			<br/> <hr color="black">
			<form method="POST" action="Recherche.php?choixAPI=1">
			<div class="container">

			<div class="text-center">
				<label for='fn'>Nom du pays :</label></br>
				<input class='form-control' type='text' name='Lpays2' id='Lpays2' placeholder='Veuillez entrer le nom du pays'/></br>
			</div>

			<br/><br/>
				 <div class="modal-footer">
					<button class="btn btn-primary" name="league2" type="submit" value="Valider">Valider</button>
			</div>
			</div>	
</form>


<?php
	}
	if($_POST["typeL"] == 2){?>
			<br/> <hr color="black">
			<form method="POST" action="Recherche.php?choixAPI=1">
			<div class="container">

			<div class="text-center">
				<label for='fn'>Nom du pays :</label></br>
				<input class='form-control' type='text' name='Lpays3' id='Lpays3' placeholder='Veuillez entrer le nom du pays'/></br>
			</div>

			<br/><br/>
				 <div class="modal-footer">
					<button class="btn btn-primary" name="league3" type="submit" value="Valider">Valider</button>
			</div>
			</div>	
		</form>

<?php 
}

	if($_POST["typeL"] == 3){
?>
<br/> <hr color="black">
			<form method="POST" action="Recherche.php?choixAPI=1">
			<div class="container">

			<div class="text-center">
				<label for='fn'>Nom du pays :</label></br>
				<input class='form-control' type='text' name='Lpays4' id='Lpays4' placeholder='Veuillez entrer le nom du pays'/></br>
			</div>
			<div class="text-center">
				<label for='fn'>Nom de la league :</label></br>
				<input class='form-control' type='text' name='Ll' id='Ll' placeholder="Veuillez entrer le nom de la league"/></br>
			</div>
			<div class="text-center">
				<label for='fn'>Année de fin :</label></br>
				<input class='form-control' type='text' name='Lanne' id='Lanne' placeholder="Veuillez entrer l'année de fin (all si toutes les années)"/></br>
			</div>
			<br/><br/>
				 <div class="modal-footer">
					<button class="btn btn-primary" name="league4" type="submit" value="Valider">Valider</button>
			</div>
			</div>	
		</form>

<?php

			}
		}
	//fin league
	}

	if($_GET["choixAPI"] == 2){

		echo "string";
	}












//fin
}
		 ?>




</body>
</html>





<?php 
//	Renvoie pour les recherche des joueur
if (isset($_POST["valPlayerJ"])) {

	if(isset($_POST["dataP"])){
	if($_POST["dataP"] == 0){
		header("Location: http://127.0.0.1:5000/?API-type=players&lastName=".$_POST["ln"]."&firstName=".$_POST["fn"]."&matches=1");
	}

	if($_POST["dataP"] == 1){
		header("Location: http://127.0.0.1:5000/?API-type=players&lastName=".$_POST["ln"]."&firstName=".$_POST["fn"]."&dataPlayer=1");
	}

	if($_POST["dataP"] == 2){
		header("Location: http://127.0.0.1:5000/?API-type=players&lastName=".$_POST["ln"]."&firstName=".$_POST["fn"]."&career=1");
	}

	if($_POST["dataP"] == 3){
		header("Location: http://127.0.0.1:5000/?API-type=players&lastName=".$_POST["ln"]."&firstName=".$_POST["fn"]."&all=1");
	}

}
}


if(isset($_POST["valPlayer"])){
	header("Location: http://127.0.0.1:5000/?API-type=players&country=".$_POST["pays"]."&club=".$_POST["club"]);
}


if(isset($_POST["league1"])){
	header("Location: http://127.0.0.1:5000/?API-type=leagues&country=".$_POST["Lpays1"]);
}

if(isset($_POST["league2"])){
	header("Location: http://127.0.0.1:5000/?API-type=leagues&country=".$_POST["Lpays2"]."&type=1");
}

if(isset($_POST["league3"])){
	header("Location: http://127.0.0.1:5000/?API-type=leagues&country=".$_POST["Lpays3"]."&all=1");
}

if(isset($_POST["league4"])){
	header("Location: http://127.0.0.1:5000/?API-type=leagues&country=".$_POST["Lpays4"]."&league=".$_POST["Ll"]."&winner=True&end-year=".$_POST["Lanne"]);
}


?>
