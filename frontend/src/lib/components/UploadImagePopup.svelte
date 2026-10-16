<script>
	import { fade, fly } from 'svelte/transition';
	import birdTarpPopupImage from '$lib/assets/bird-tarp-popup.png';

	let { isOpen = $bindable(false) } = $props();

	function close() {
		isOpen = false;
	}
</script>

<svelte:window onkeydown={(event) => event.key === 'Escape' && close()} />

{#if isOpen}
	<div
		class="fixed inset-0 z-20 grid place-items-center bg-black/55 p-6 backdrop-blur-sm"
		transition:fade={{ duration: 220 }}
		role="button"
		tabindex="0"
		aria-label="Close upload image popup"
		onclick={(event) => event.currentTarget === event.target && close()}
		onkeydown={(event) =>
			(event.key === 'Enter' || event.key === ' ') && event.currentTarget === event.target && close()}
	>
		<div
			class="relative flex h-120 w-110 flex-col items-center bg-reds-300"
			role="dialog"
			aria-modal="true"
			aria-label="Upload image popup"
			tabindex="-1"
			in:fly={{ y: -1000, duration: 320, easing: (t) => 1 - (1 - t) ** 3 }}
			out:fly={{ y: -1000, duration: 260 }}
		>
			<img class="-mt-[12%] h-full w-full" src={birdTarpPopupImage} alt="Bird tarp" />
			<div class="absolute h-full w-full opacity-50">
        <div class="absolute bg-green-300 w-[60%] h-[41%] top-[26%] left-[20%]"> </div>
				<button class="absolute top-[58%] left-[22%] h-[7%] w-[56%]" aria-label="Select image"></button>
				<button class="absolute top-[73%] left-[24%] h-[9%] w-[52%]" aria-label="Upload image"></button>
			</div>
		</div>
	</div>
{/if}
