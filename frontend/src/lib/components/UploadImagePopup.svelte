<script>
	import { onDestroy } from 'svelte';
	import { fade, fly } from 'svelte/transition';
	import birdTarpPopupImage from '$lib/assets/bird-tarp-popup.png';

  const serverUrl = import.meta.env.VITE_SERVER_URL

	/** @typedef {{ job_title: string, kapalaran_score: number, explanation: string }} PalmPrediction */
	let { isOpen = $bindable(false), onPrediction = () => {} } = $props();

	let fileInput = $state(/** @type {HTMLInputElement | undefined} */ (undefined));
	let selectedImage = $state();
	let previewUrl = $state();
	let isUploading = $state(false);
	let errorMessage = $state('');

	function close() {
		isOpen = false;
	}

	function selectImage() {
		fileInput?.click();
	}

	/** @param {Event & { currentTarget: HTMLInputElement }} event */
	function handleImageSelection(event) {
		const image = event.currentTarget.files?.[0];
		if (!image) return;

		if (!image.type.startsWith('image/')) {
			errorMessage = 'Please select an image file.';
			return;
		}

		if (previewUrl) URL.revokeObjectURL(previewUrl);
		selectedImage = image;
		previewUrl = URL.createObjectURL(image);
		errorMessage = '';
	}

	async function uploadImage() {
		if (!selectedImage) {
			errorMessage = 'Select a palm image first.';
			return;
		}

		isUploading = true;
		errorMessage = '';

		try {
			const formData = new FormData();
			formData.append('image', selectedImage);

			const response = await fetch(`${serverUrl}/api/v1/palm-scan-prediction`, {
				method: 'POST',
				body: formData
			});
			const result = await response.json().catch(() => ({}));

			if (!response.ok) {
				throw new Error(result.error?.message || 'Unable to create a prediction. Please try again.');
			}

			onPrediction(/** @type {PalmPrediction} */ (result));
			close();
		} catch (error) {
			errorMessage = error instanceof Error ? error.message : 'Unable to create a prediction. Please try again.';
		} finally {
			isUploading = false;
		}
	}

	onDestroy(() => previewUrl && URL.revokeObjectURL(previewUrl));
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
			<div class="absolute h-full w-full">
				<div class="absolute top-[24.9%] left-[19%] h-[43.3%] w-[63.2%] overflow-hidden">
					{#if previewUrl}
						<img class="h-full w-full rounded-sm object-cover" src={previewUrl} alt="Selected palm" />
					{/if}
				</div>
				<input bind:this={fileInput} class="sr-only" type="file" accept="image/*" onchange={handleImageSelection} />
				<button type="button" class="absolute top-[58%] left-[22%] h-[7%] w-[56%]" aria-label="Select image" onclick={selectImage}></button>
				<button type="button" class="absolute top-[73%] left-[24%] h-[9%] w-[52%]" aria-label="Upload image" onclick={uploadImage} disabled={isUploading}></button>
				{#if errorMessage}
					<p class="absolute inset-x-[15%] bottom-[4%] text-center text-xs text-red-950" role="alert">{errorMessage}</p>
				{/if}
			</div>
		</div>
	</div>
{/if}
