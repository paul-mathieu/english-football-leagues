<?php
ob_start()
?>

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
		  <label class="form-check-label" for="materialInline5">Transfer &nbsp &nbsp &nbsp</label>
		</div>
		<div class="form-check form-check-inline">
		<div class="checkbox">
  			<label><input type="checkbox" id ="csv" name="csv" value="1">Sauvegarde CSV</label>
		</div>
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
				<form method="POST">
			
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
				<form method="POST">
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
		<form method="POST">
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
			<form method="POST">
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
			<form method="POST">
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
			<form method="POST">
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

	if($_GET["choixAPI"] == 2){?>
			<br/>
			<hr color="black">
			<form method="POST">
				<div class="text-center">

				<div class="form-check form-check-inline">
				  <input type="radio" class="form-check-input" id="Joueur" name="typeM" value="0" onchange="this.form.submit()">
				  <label class="form-check-label" for="materialInline1">Ensemble des matchs d'une journée</label>
				</div>

				<div class="form-check form-check-inline">
				  <input type="radio" class="form-check-input" id="League" name="typeM" value="1" onchange="this.form.submit()">
				  <label class="form-check-label" for="materialInline2">Votre match</label>
				</div>
			</div>
		

		<?php
		
		if(isset($_POST["typeM"])){
		if($_POST["typeM"] == 0){?>
		<br/> <hr color="black">
			<form method="POST">
			<div class="container">

			<div class="text-center">
				<label for='fn'>Jours :</label></br>
				<input class='form-control' type='text' name='j' id='j' placeholder='Veuillez entrer le jour (format dd)'/></br>
			</div>


			<div class="text-center">
				<label for='fn'>Mois :</label></br>
				<input class='form-control' type='text' name='m' id='m' placeholder='Veuillez entrer le mois (format mm)'/></br>
			</div>


			<div class="text-center">
				<label for='fn'>Année :</label></br>
				<input class='form-control' type='text' name='a' id='a' placeholder="Veuillez entrer l'année (format yyyy)"/></br>
			</div>

			<br/><br/>
				 <div class="modal-footer">
					<button class="btn btn-primary" name="match1" type="submit" value="Valider">Valider</button>
			</div>
		</div>
	</form>




<?php
	}
			if($_POST["typeM"] == 1){?>
			<br/> <hr color="black">
			<form method="POST">
			<div class="container">

			<div class="text-center">
				<label for='fn'>Equipe A</label></br>
				<input class='form-control' type='text' name='clA' id='clA' placeholder="Nom de l'équipe A"/></br>
			</div>


			<div class="text-center">
				<label for='fn'>Pays A</label></br>
				<input class='form-control' type='text' name='pA' id='pA' placeholder="Pays de l'équipe A"/></br>
			</div>


			<div class="text-center">
				<label for='fn'>Equipe B</label></br>
				<input class='form-control' type='text' name='clB' id='clB' placeholder="Nom de l'équipe B"/></br>
			</div>


			<div class="text-center">
				<label for='fn'>Pays B</label></br>
				<input class='form-control' type='text' name='pB' id='pB' placeholder="Pays de l'équipe B"/></br>
			</div>

			<br/><br/>
				 <div class="modal-footer">
					<button class="btn btn-primary" name="match2" type="submit" value="Valider">Valider</button>
			</div>
		</div>
	</form>
<?php
}
}
}


if($_GET["choixAPI"] == 4){?>

<br/> <hr color="black">
<form method="POST">
			<div class="container">

			<div class="text-center">
				<label for='fn'>Equipe</label></br>
				<input class='form-control' type='text' name='trC' id='trC' placeholder="Nom de l'équipe"/></br>
			</div>


			<div class="text-center">
				<label for='fn'>Année</label></br>
				<input class='form-control' type='text' name='ye' id='ye' placeholder="Année format (yyyy)"/></br>
			</div>
			<br/><br/>
				 <div class="modal-footer">
					<button class="btn btn-primary" name="transfer" type="submit" value="Valider">Valider</button>
			</div>
		</div>
	</form>




<?php
}
if($_GET["choixAPI"] == 3){?>
	<br/> <hr color="black">
<form method="POST">
	<div class="container">
		<div class="text-center">
			<label for='fn'>Equipe</label></br>
			<input class='form-control' type='text' name='t' id='t' placeholder="Nom de l'équipe"/></br>
		</div>

		<div class="text-center">
			<label for='fn'>Nombre de résultat</label></br>
			<input class='form-control' type='text' name='nb' id='nb' placeholder="Nombre de résultat (entier)"/></br>
		</div>
<br/>

		<div class="text-center">Retourne les infos d’une équipe  :
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="a" value="True">
			<label class="form-check-label" for="materialInline2">Oui</label>
		</div>
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="a" value="False">
			<label class="form-check-label" for="materialInline2">Non</label>
		</div></div><br/><br/>

		<div class="text-center">Retourne les informations sur le stade de l’équipe  :
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="b" value="True">
			<label class="form-check-label" for="materialInline2">Oui</label>
		</div>
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="b" value="False">
			<label class="form-check-label" for="materialInline2">Non</label>
		</div></div><br/><br/>

		<div class="text-center">Retourne la liste des trophées obtenus depuis la création de l’équipe  :
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="c" value="True">
			<label class="form-check-label" for="materialInline2">Oui</label>
		</div>
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="c" value="False">
			<label class="form-check-label" for="materialInline2">Non</label>
		</div></div><br/><br/>

		<div class="text-center">Retourne les 50 derniers matchs  :
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="d" value="True">
			<label class="form-check-label" for="materialInline2">Oui</label>
		</div>
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="d" value="False">
			<label class="form-check-label" for="materialInline2">Non</label>
		</div></div><br/><br/>
	

		<div class="text-center">Retourne la composition de l’équipe  :
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="e" value="True">
			<label class="form-check-label" for="materialInline2">Oui</label>
		</div>
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League"name="e" value="False">
			<label class="form-check-label" for="materialInline2">Non</label>
		</div></div><br/><br/>

		<div class="text-center">Retourne la liste de tous les sites de fans  :
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="f" value="True">
			<label class="form-check-label" for="materialInline2">Oui</label>
		</div>
		<div class="form-check form-check-inline">
			<input type="radio" class="form-check-input" id="League" name="f" value="False">
			<label class="form-check-label" for="materialInline2">Non</label>
		</div></div><br/>
	

	<br/><br/>
		<div class="modal-footer">
			<button class="btn btn-primary" name="mat" type="submit" value="Valider">Valider</button>
		</div>

	</div>
</form>
<?php	
}
}
?>




</body>
</html>





<?php 
$csvV = "";
if(isset($_GET["csv"])){
	$csvV = "&import=csv";
}

//	Renvoie pour les recherche des joueur
if (isset($_POST["valPlayerJ"])) {

	if(isset($_POST["dataP"])){
	if($_POST["dataP"] == 0){
		header("Location: http://127.0.0.1:5000/?API-type=players&lastName=".$_POST["ln"]."&firstName=".$_POST["fn"]."&matches=1".$csvV);
	}

	if($_POST["dataP"] == 1){

		header("Location: http://127.0.0.1:5000/?API-type=players&lastName=".$_POST["ln"]."&firstName=".$_POST["fn"]."&dataPlayer=1".$csvV);
	}

	if($_POST["dataP"] == 2){
		header("Location: http://127.0.0.1:5000/?API-type=players&lastName=".$_POST["ln"]."&firstName=".$_POST["fn"]."&career=1".$csvV);
	}

	if($_POST["dataP"] == 3){
		header("Location: http://127.0.0.1:5000/?API-type=players&lastName=".$_POST["ln"]."&firstName=".$_POST["fn"]."&all=1".$csvV);
	}

}
}


if(isset($_POST["valPlayer"])){
	header("Location: http://127.0.0.1:5000/?API-type=players&country=".$_POST["pays"]."&club=".$_POST["club"].$csvV);
}


if(isset($_POST["league1"])){
	header("Location: http://127.0.0.1:5000/?API-type=leagues&country=".$_POST["Lpays1"].$csvV);
}

if(isset($_POST["league2"])){
	header("Location: http://127.0.0.1:5000/?API-type=leagues&country=".$_POST["Lpays2"]."&type=True".$csvV);
}

if(isset($_POST["league3"])){
	header("Location: http://127.0.0.1:5000/?API-type=leagues&country=".$_POST["Lpays3"]."&all=True".$csvV);
}

if(isset($_POST["league4"])){
	header("Location: http://127.0.0.1:5000/?API-type=leagues&country=".$_POST["Lpays4"]."&league=".$_POST["Ll"]."&winner=True&end-year=".$_POST["Lanne"].$csvV);
}


if(isset($_POST["match1"])){
	header("Location: http://127.0.0.1:5000/?API-type=match&all=True&m=".$_POST["m"]."&d=".$_POST["j"]."&y=".$_POST["a"].$csvV);
}

if(isset($_POST["match2"])){
	header("Location: http://127.0.0.1:5000/?API-type=match&clubA=".$_POST["clA"]."&clubB=".$_POST["clB"]."&countryA=".$_POST["pA"]."&countryB=".$_POST["pB"].$csvV);
}

if(isset($_GET["choixAPI"]) AND $_GET["choixAPI"] == 4 and isset($_POST["transfer"])){
	header("Location: http://127.0.0.1:5000/?API-type=transfer&team=".$_POST["trC"]."&year=".$_POST["ye"].$csvV);
}

if(isset($_GET["choixAPI"]) AND $_GET["choixAPI"] == 3 and isset($_POST["mat"])){
	//echo "Location: http://127.0.0.1:5000/?API-type=teams&name-team=".$_POST["t"]."&max-result=".$_POST["nb"]."&info=".$_POST["a"]."&venue=".$_POST["b"]."&trophies=".$_POST["c"]."&squad=".$_POST["d"]."&squad-info=".$_POST["e"]."&fan-sites=".$_POST["f"];
	header("Location: http://127.0.0.1:5000/?API-type=teams&name-team=".$_POST["t"]."&max-result=".$_POST["nb"]."&info=".$_POST["a"]."&venue=".$_POST["b"]."&trophies=".$_POST["c"]."&matches=".$_POST["d"]."&squad=".$_POST["e"]."&squad-info=".$_POST["e"]."&fan-sites=".$_POST["f"]);
}
//Location: http://127.0.0.1:5000/?API-type=teams&name-team=Liverpool&max-result=1&info=True&venue=False&trophies=False&squad=False&squad-info=False&fan-sites=False
ob_end_flush();
?>

 