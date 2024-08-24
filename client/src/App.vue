<template>
  <!-- bg-[url('./assets/cinema-background-pattern_1061-5.png')] -->
  <div class="w-full h-screen flex flex-col overflow-hidden">
    <div
      class="absolute inset-0 -z-10 h-full w-full bg-white bg-[radial-gradient(#e5e7eb_1px,transparent_1px)] [background-size:16px_16px]"
    ></div>
    <div
      class="w-full h-full flex flex-col items-center overflow-auto"
      :class="
        !results || results.length === 0 ? 'justify-center' : 'justify-start'
      "
    >
      <div class="w-full max-w-3xl py-3">
        <div
          class="w-full flex flex-row justify-center items-center gap-5 py-5"
        >
          <div>
            <img src="./assets/logo.png" alt="logo" class="w-16 h-16" />
          </div>
          <div>
            <div>
              <div
                class="text-3xl font-bold bg-gradient-to-r from-blue-600 via-green-500 to-indigo-400 inline-block text-transparent bg-clip-text"
              >
                PlotFinder
              </div>
              <div>Discover films by their storylines.</div>
            </div>
          </div>
        </div>
        <div class="px-3">
          <textarea
            v-model="plot"
            class="w-full h-24 bg-white p-2 rounded-lg shadow focus:shadow-lg focus:outline-none focus:ring-0 focus:ring-blue-500 focus:border-transparent"
            placeholder="Enter a movie plot here..."
          ></textarea>
        </div>
        <div>
          <div class="w-full flex justify-end px-3">
            <button
              @click="search"
              class="bg-blue-500 text-white px-7 py-2 rounded-xl shadow focus:shadow-lg focus:outline-none focus:ring-0 focus:ring-blue-500 focus:border-transparent flex gap-3"
            >
              <svg
                v-if="isLoading"
                aria-hidden="true"
                class="w-5 h-5 text-gray-200 animate-spin dark:text-gray-600 fill-white"
                viewBox="0 0 100 101"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                  fill="currentColor"
                />
                <path
                  d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                  fill="currentFill"
                />
              </svg>
              Search
            </button>
          </div>
        </div>
        <div class="w-full flex justify-center text-sm text-neutral-500">
          <!-- search over a million movies -->
          Find your next watch among nearly a million movies.
        </div>
      </div>
      <div
        class="w-full h-full flex justify-center"
        v-if="results && results.length > 0"
      >
        <div class="w-full h-full max-w-3xl">
          <div class="w-full text-xl pb-2 border-b-[1px] border-neutral-300">
            Results
          </div>
          <div class="w-full flex flex-col gap-3 py-3">
            <div
              v-for="(result, index) in results"
              class="w-full flex flex-row gap-3 border-neutral-100 border-b-[1px]"
            >
              <div class="flex-none">
                <img
                  v-if="result?.metadata?.poster_path"
                  :src="
                    'https://image.tmdb.org/t/p/w600_and_h900_bestv2' +
                    result?.metadata?.poster_path
                  "
                  alt="poster"
                  class="w-40 h-60 object-cover rounded"
                />
                <div
                  class="w-40 h-60 bg-neutral-300 text-neutral-500 flex justify-center items-center rounded"
                  v-else
                >
                  No Poster
                </div>
              </div>
              <div>
                <div class="p-3">
                  <div class="text-xl font-bold">
                    {{ result?.metadata?.title }}
                  </div>
                  <div class="text-sm">
                    Release Date:
                    {{ result?.metadata?.release_date }}
                  </div>
                </div>
                <div>
                  <div class="p-3">
                    <div class="text-lg font-bold">Overview</div>
                    <div class="text-sm">{{ result?.metadata?.overview }}</div>
                  </div>
                </div>
                <div>
                  <div class="p-3">
                    <div class="text-lg font-bold">Genres</div>
                    <div class="text-sm">
                      {{
                        result?.metadata?.genres
                          ?.map((genre) => genre.name)
                          .join(", ")
                      }}
                    </div>
                  </div>
                </div>
                <div>
                  <div class="p-3">
                    <div class="text-lg font-bold">Rating</div>
                    <div class="text-sm">
                      {{ result?.metadata?.vote_average }}
                    </div>
                  </div>
                </div>
              </div>
              <!-- {{ result }} -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="w-full flex justify-center p-3">
      <div>
        <div class="text-sm">Powered by</div>
        <div class="flex items-center gap-3 px-3 pb-3 py-1">
          <img
            src="https://static.pingcap.com/files/2023/07/09063705/TiDB-logo.png"
            alt="tidb"
            class="w-10"
          />
          <span class="text-xl text-neutral-500"> x </span>
          <img
            src="https://s3.amazonaws.com/challengepost/sponsors/logos/000/035/966/highres/Company_logo_light_2x_%289%29.png"
            alt="jina.ai"
            class="w-24"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      plot: "",
      results: [],
      isLoading: false,
    };
  },
  methods: {
    search() {
      // console.log(this.plot);
      this.results = [];
      this.isLoading = true;
      const url = import.meta.env.VITE_API_URL;
      // console.log(url);
      axios
        .post(url, {
          query: this.plot,
        })
        .then((response) => {
          console.log(response.data);
          this.results = response.data;
          this.isLoading = false;
        })
        .catch((error) => {
          console.error(error);
          this.isLoading = false;
        });
    },
  },
};
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap");

* {
  font-family: "Poppins", sans-serif;
}
</style>
