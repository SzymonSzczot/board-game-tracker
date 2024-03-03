
<style>
    #playerName {
      border-color: orange;
      border-width: 5px;
      border-style: solid;
    }

    .container {
      padding: 2rem;
    }

</style>

<script>
    import Timer from './Timer.svelte'
    let name = "Szymon";
    let time1 = "10:10"
    let time2 = "11:11"
    let time3 = "33:33"


</script>

<div class="container text-center">
  <div class="row align-items-center">
    <div class="col-sm-12 col-md-6 col-lg-4">
      <div id="playerName" class="p-3">
        {name}
        <div>Miejsce 1</div>
      </div>
    </div>
    <div class="col-sm-12 col-md-6 col-lg-8">
      <div class="row">
        <div class="col-sm-4">
          <Timer time={time1} description="Czas gry"></Timer>
        </div>
        <div class="col-sm-4">
          <Timer time={time2} description="Twój czas"></Timer>
        </div>
        <div class="col-sm-4">
          <Timer time={time3} description="Tura"></Timer>
        </div>
      </div>
    </div>
  </div>
</div>
