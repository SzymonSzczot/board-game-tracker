<script lang="ts">
  import Header from '../src/components/Header.svelte'
  import CurrentState from '../src/components/CurrentState.svelte'
  import Options from '../src/components/Options.svelte'
</script>


<main>

  <div class="container my-5">
      <Header></Header>
  </div>

  <div class="b-example-divider"></div>

  <div class="px-4 pt-5 my-5 text-center border-bottom">
    <CurrentState></CurrentState>
  </div>

  <div class="b-example-divider"></div>


  <div class="container my-5">
    <div class="row p-4 pb-0 pe-lg-0 pt-lg-5 align-items-center rounded-3 border shadow-lg">
      <Options></Options>
    </div>
  </div>


  <div class="b-example-divider mb-0"></div>
</main>
