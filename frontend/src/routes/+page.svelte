<script>
	import '@fontsource/henny-penny';
	import { fade, fly } from 'svelte/transition';
	import menuTarpImage from '$lib/assets/menu-tarp.png';
	import handIconImage from '$lib/assets/hand-icon.png';
	import birdTarpPopupImage from '$lib/assets/bird-tarp-popup.png';
	import witchImage from '$lib/assets/whitch.png';

	let isBirdPopupOpen = $state(false);
</script>

<svelte:window onkeydown={(event) => event.key === 'Escape' && (isBirdPopupOpen = false)} />

<main class="night-sky relative isolate min-h-svh overflow-hidden bg-[#020817]">
	<header class="relative z-10 px-6 pt-8 text-center sm:pt-12">
		<h1 class="mb-15 font-['Henny_Penny'] text-4xl tracking-[0.2em] text-yellow-100 drop-shadow-lg sm:text-6xl">
		  Palad Gpt	
		</h1>
	</header>

  <div class="w-full flex flex-row items-center justify-center gap-15">
    <img
      src={witchImage}
      alt="Witch"
      class="min-w-60 max-w-110"
    />
    
    <div class="relative w-70 -ml-10 -mt-10 flex items-center justify-center">
      <div class="bg-tranparent w-full h-full absolute opacity-100">
        <button
			type="button"
			class="flex flex-col items-center justify-center absolute w-[23%] top-[22%] left-[29%] aspect-[10/11] h-auto bg-transparent opacity-100"
			onclick={() => (isBirdPopupOpen = true)}
			aria-label="Open bird popup"
		>
          <img class="menu-icon w-4/5" src={handIconImage} alt="Hand" />
        </button>
        <button class="absolute w-[23%] top-[22%] left-[57%] aspect-[100/113] h-auto bg-transparent opacity-100"> </button>
        <button class="absolute w-[23%] top-[41%] left-[29%] aspect-[10/11] h-auto bg-transparent opacity-100"> </button>
        <button class="absolute w-[23%] top-[42%] left-[57%] aspect-[10/11] h-auto bg-transparent opacity-100"> </button>
        <button class="absolute w-[23%] top-[60%] left-[29%] aspect-[100/114] h-auto bg-transparent opacity-100"> </button>
        <button class="absolute w-[23%] top-[60%] left-[57%] aspect-[100/112] h-auto bg-transparent opacity-100"> </button>
      </div>

      <img
        src={menuTarpImage}
        alt="Menu tarp"
        class="w-full"
      />
    </div>
  </div>

	{#if isBirdPopupOpen}
		<div
			class="fixed inset-0 z-20 grid place-items-center bg-black/55 p-6 backdrop-blur-sm"
			transition:fade={{ duration: 220 }}
			role="button"
			tabindex="0"
			aria-label="Close bird popup"
			onclick={() => (isBirdPopupOpen = false)}
		>
			<div
				class="relative w-110 h-120 bg-reds-300 flex flex-col items-center"
				role="dialog"
				aria-modal="true"
				aria-label="Bird popup"
				in:fly={{ y: -1000, duration: 320, easing: (t) => 1 - (1 - t) ** 3 }}
				out:fly={{ y: -1000, duration: 260 }}
				onclick={(event) => event.stopPropagation()}
			>
				<img class="h-full w-full -mt-[12%]" src={birdTarpPopupImage} alt="Bird tarp" />
        <div class="h-full w-full opacity-50 absolute"> 
          <button class="absolute bg-green-300 w-[56%] h-[7%] top-[58%] left-[22%]"> </button> 
          <button class="absolute bg-green-300 w-[52%] h-[9%] top-[73%] left-[24%]"> </button> 
        </div>

			</div>
		</div>
	{/if}
</main>

<style>
	.night-sky {
		background-image:
			radial-gradient(ellipse at 50% 100%, #172852 0%, transparent 55%),
			radial-gradient(ellipse at 75% 20%, #101d41 0%, transparent 45%);
	}

	.night-sky::before,
	.night-sky::after {
		position: absolute;
		inset: -10%;
		z-index: -1;
		content: '';
		background-repeat: repeat;
		will-change: background-position;
	}

	.night-sky::before {
		opacity: 0.9;
		background-image:
			radial-gradient(1.5px 1.5px at 12% 18%, #fff 99%, transparent),
			radial-gradient(1px 1px at 72% 12%, #dce9ff 99%, transparent),
			radial-gradient(1px 1px at 38% 67%, #fff 99%, transparent),
			radial-gradient(1.5px 1.5px at 87% 78%, #e8f2ff 99%, transparent),
			radial-gradient(1px 1px at 19% 90%, #fff 99%, transparent),
			radial-gradient(1px 1px at 57% 42%, #cbdcff 99%, transparent);
		background-size: 193px 227px, 251px 179px, 317px 281px, 229px 337px, 359px 263px, 277px 311px;
		animation: drift 80s linear infinite;
	}

	.night-sky::after {
		opacity: 0.65;
		background-image:
			radial-gradient(2px 2px at 24% 24%, #fff 99%, transparent),
			radial-gradient(1.5px 1.5px at 66% 48%, #d7e5ff 99%, transparent),
			radial-gradient(1.5px 1.5px at 82% 83%, #fff 99%, transparent),
			radial-gradient(1px 1px at 43% 88%, #fff 99%, transparent);
		background-size: 431px 389px, 503px 461px, 367px 547px, 619px 421px;
		filter: drop-shadow(0 0 3px rgb(210 228 255 / 0.7));
		animation: drift-reverse 130s linear infinite;
	}

	@keyframes drift {
		to {
			background-position: 70px 110px, -90px 70px, 130px -80px, -70px -120px, 100px 50px, -110px 90px;
		}
	}

	@keyframes drift-reverse {
		to {
			background-position: -80px -120px, 110px -70px, -100px 90px, 130px 100px;
		}
	}

	@media (prefers-reduced-motion: reduce) {
		.night-sky::before,
		.night-sky::after {
			animation: none;
		}
	}

	.menu-icon {
		transition: transform 150ms ease-out;
	}

	.menu-icon:hover {
		transform: scale(1.1);
	}

</style>
