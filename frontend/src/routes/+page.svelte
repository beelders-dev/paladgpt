<main
	class="night-sky relative isolate min-h-svh overflow-hidden bg-[#020817]"
	aria-label="Starry night sky"
></main>

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
</style>
