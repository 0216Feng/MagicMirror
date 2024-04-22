// Initially display infomation
async function displayCourses() {
    const countText = document.getElementById('courseCount');
    const courseInfo = document.getElementById('courseInfo');

    try {
        let response = await fetch('/getCourses');
        let data = await response.json();

        let course = data["course"];
        let count = data["count"];
        countText.innerHTML = `${count}`;
        let htmlContent = '';

        for (let i = 0; i < count; i++) {
            let cid = course[i]["CID"]
            let name = course[i]["Name"]
            let time = course[i]["Time"]
            let location = course[i]["Location"]
            let week = course[i]["Week"]
            let description = course[i]["Description"]

            if (!location || location == '') {
                location = '无'
            }
            
            let text = `<div class="relative flex flex-col items-start p-4 mt-3 bg-white rounded-lg cursor-pointer bg-opacity-90 group hover:bg-opacity-100" draggable="true">
                    <button class="courseDelete absolute top-0 right-0 flex items-center justify-center hidden w-5 h-5 mt-3 mr-2 text-gray-500 rounded hover:bg-gray-200 hover:text-gray-700 group-hover:flex" cid="${cid}">
                        <svg t="1713527777962" class="icon" viewBox="0 0 1025 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6969" width="15" height="15">
                            <path d="M548.316196 512l468.011988-468.011988c10.22977-10.22977 10.22977-26.085914 0-36.315684s-26.085914-10.22977-36.315684 0L512.000511 475.684316 43.988523 8.183816c-10.22977-10.22977-26.085914-10.22977-36.315684 0s-10.22977 26.085914 0 36.315684L475.684827 512 8.184328 980.011988c-10.22977 10.22977-10.22977 26.085914 0 36.315684 5.114885 5.114885 11.764236 7.672328 17.902098 7.672328s13.298701-2.557443 17.902097-7.672328l468.011988-468.011988 468.011989 468.011988c5.114885 5.114885 11.764236 7.672328 17.902097 7.672328s13.298701-2.557443 17.902098-7.672328c10.22977-10.22977 10.22977-26.085914 0-36.315684L548.316196 512z" fill="#8a8a8a" p-id="6970"></path>
                        </svg>
                    </button>
                    <span class="flex items-center h-6 px-3 text-xs font-semibold text-blue-500 bg-blue-100 rounded-full">Course</span>
                    <h4 class="mt-3 text-md font-medium"><b>${name}</b></h4>
                    <p class="mt-3 text-sm text-gray-500">${description}</p>
                    <div class="flex items-center w-full mt-3 text-xs font-medium text-gray-400">
                        <div class="flex items-center">
                            <svg class="w-4 h-4 text-gray-300 fill-current" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z" clip-rule="evenodd" />
                            </svg>
                            <span class="ml-1 leading-none">${week} ${time}</span>
                        </div>
                        <div class="relative flex items-center ml-auto">
                            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" t="1713467264420" class="icon" viewBox="0 0 1024 1024" version="1.1" p-id="4273" width="22" height="22">
                                    <path d="M503.23456 885.82144l-14.04928-14.15168C478.02368 860.38528 215.49056 593.92 215.49056 434.7904c0-163.55328 129.29024-296.61184 288.21504-296.61184 158.90432 0 288.21504 132.28032 288.256 294.87104 0.04096 159.0272-271.4624 436.51072-274.20672 439.07072l-14.52032 13.70112z m0.49152-706.6624c-136.33536 0-247.25504 114.688-247.25504 255.65184 0 122.79808 192.7168 335.21664 247.48032 393.09312C563.2 765.62432 751.06304 549.4784 751.02208 433.07008c-0.04096-140.00128-110.98112-253.91104-247.296-253.91104z m1.88416 360.83712c-68.9152 0-125.00992-57.79456-125.00992-128.83968s56.07424-128.8192 125.00992-128.8192c68.89472 0 124.96896 57.79456 124.96896 128.8192s-56.05376 128.83968-124.96896 128.83968z m0-216.6784c-46.34624 0-84.04992 39.40352-84.04992 87.8592s37.70368 87.8592 84.04992 87.8592c46.32576 0 84.00896-39.40352 84.00896-87.8592s-37.6832-87.8592-84.00896-87.8592z" fill="#bfbfbf" p-id="4274"/>
                            </svg>
                            <span class="ml-1 leading-none">${location}</span>
                        </div>
                    </div>
                </div>`;
            htmlContent += text;
        }

        courseInfo.innerHTML = htmlContent;
    }
    catch (error) {
        console.log(error);
    }
}

async function displaySchedule() {
    const countText = document.getElementById('scheduleCount');
    const courseInfo = document.getElementById('scheduleInfo');

    try {
        let response = await fetch('/getSchedules');
        let data = await response.json();
        let schedule = data["schedule"];
        let count = data["count"];
        countText.innerHTML = `${count}`;
        let htmlContent = '';

        for (let i = 0; i < count; i++) {
            let sid = schedule[i]["SID"]
            let name = schedule[i]["Name"]
            let time = schedule[i]["Time"]
            let location = schedule[i]["Location"]
            let description = schedule[i]["Description"]
            let [day, times] = time.split(' ');

            if (!location || location == '') {
                location = '无'
            }

            let text = `<div class="relative flex flex-col items-start p-4 mt-3 bg-white rounded-lg cursor-pointer bg-opacity-90 group hover:bg-opacity-100" draggable="true">
                    <button class="scheduleDelete absolute top-0 right-0 flex items-center justify-center hidden w-5 h-5 mt-3 mr-2 text-gray-500 rounded hover:bg-gray-200 hover:text-gray-700 group-hover:flex" sid="${sid}">
                        <svg t="1713527777962" class="icon" viewBox="0 0 1025 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6969" width="15" height="15">
                            <path d="M548.316196 512l468.011988-468.011988c10.22977-10.22977 10.22977-26.085914 0-36.315684s-26.085914-10.22977-36.315684 0L512.000511 475.684316 43.988523 8.183816c-10.22977-10.22977-26.085914-10.22977-36.315684 0s-10.22977 26.085914 0 36.315684L475.684827 512 8.184328 980.011988c-10.22977 10.22977-10.22977 26.085914 0 36.315684 5.114885 5.114885 11.764236 7.672328 17.902098 7.672328s13.298701-2.557443 17.902097-7.672328l468.011988-468.011988 468.011989 468.011988c5.114885 5.114885 11.764236 7.672328 17.902097 7.672328s13.298701-2.557443 17.902098-7.672328c10.22977-10.22977 10.22977-26.085914 0-36.315684L548.316196 512z" fill="#8a8a8a" p-id="6970"></path>
                        </svg>
                    </button>
                    <span class="flex items-center h-6 px-3 text-xs font-semibold text-pink-500 bg-pink-100 rounded-full">Schedule</span>
                    <h4 class="mt-3 text-md font-medium"><b>${name}</b></h4>
                    <p class="mt-3 text-sm text-gray-500">${description}</p>
                    <div class="flex items-center w-full mt-3 text-xs font-medium text-gray-400">
                        <div class="flex items-center">
                            <svg t="1713520227169" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4317" width="16" height="16">
                                <path d="M513.871 21.19c-271.033 0-491.52 220.487-491.52 491.52s220.487 491.52 491.52 491.52 491.52-220.487 491.52-491.52-220.487-491.52-491.52-491.52zM513.871 963.27c-248.436 0-450.56-202.124-450.56-450.56s202.124-450.56 450.56-450.56 450.56 202.124 450.56 450.56-202.124 450.56-450.56 450.56z" fill="#bfbfbf" p-id="4318"></path><path d="M769.516 570.737l-314.669 0.041v-314.491c0-11.264-9.216-20.48-20.48-20.48s-20.48 9.216-20.48 20.48c0 0-0.041 334.739-0.041 334.971 0 11.264 9.216 20.48 20.48 20.48l335.175-0.041c11.264 0 20.48-9.216 20.48-20.48 0.014-11.264-9.202-20.48-20.466-20.48z" fill="#bfbfbf" p-id="4319"></path>
                            </svg>
                            <span class="ml-1 leading-none items-center">${day}<br />${times}</span>
                            
                        </div>
                        <div class="relative flex items-center ml-auto">
                            <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" t="1713467264420" class="icon" viewBox="0 0 1024 1024" version="1.1" p-id="4273" width="22" height="22">
                                    <path d="M503.23456 885.82144l-14.04928-14.15168C478.02368 860.38528 215.49056 593.92 215.49056 434.7904c0-163.55328 129.29024-296.61184 288.21504-296.61184 158.90432 0 288.21504 132.28032 288.256 294.87104 0.04096 159.0272-271.4624 436.51072-274.20672 439.07072l-14.52032 13.70112z m0.49152-706.6624c-136.33536 0-247.25504 114.688-247.25504 255.65184 0 122.79808 192.7168 335.21664 247.48032 393.09312C563.2 765.62432 751.06304 549.4784 751.02208 433.07008c-0.04096-140.00128-110.98112-253.91104-247.296-253.91104z m1.88416 360.83712c-68.9152 0-125.00992-57.79456-125.00992-128.83968s56.07424-128.8192 125.00992-128.8192c68.89472 0 124.96896 57.79456 124.96896 128.8192s-56.05376 128.83968-124.96896 128.83968z m0-216.6784c-46.34624 0-84.04992 39.40352-84.04992 87.8592s37.70368 87.8592 84.04992 87.8592c46.32576 0 84.00896-39.40352 84.00896-87.8592s-37.6832-87.8592-84.00896-87.8592z" fill="#bfbfbf" p-id="4274"/>
                            </svg>
                            <span class="ml-1 leading-none">${location}</span>
                        </div>
                    </div>
                </div>`;
            htmlContent += text;
        }

        courseInfo.innerHTML = htmlContent;
    }
    catch (error) {
        console.log(error);
    }
}

async function displayTips() {
    const countText = document.getElementById('tipsCount');
    const courseInfo = document.getElementById('tipsInfo');

    try {
        let response = await fetch('/getTips');
        let data = await response.json();
        let tips = data["tip"];
        let count = data["count"];
        countText.innerHTML = `${count}`;
        let htmlContent = '';

        for (let i = 0; i < count; i++) {
            let tid = tips[i]["TID"]
            let time = tips[i]["Published"]
            let name = tips[i]["Title"]
            let description = tips[i]["Description"]

            let text = `<div class="relative flex flex-col items-start p-4 mt-3 bg-white rounded-lg cursor-pointer bg-opacity-90 group hover:bg-opacity-100" draggable="true">
                    <button class="tipsDelete absolute top-0 right-0 flex items-center justify-center hidden w-5 h-5 mt-3 mr-2 text-gray-500 rounded hover:bg-gray-200 hover:text-gray-700 group-hover:flex" tid="${tid}">
                        <svg t="1713527777962" class="icon" viewBox="0 0 1025 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6969" width="15" height="15">
                            <path d="M548.316196 512l468.011988-468.011988c10.22977-10.22977 10.22977-26.085914 0-36.315684s-26.085914-10.22977-36.315684 0L512.000511 475.684316 43.988523 8.183816c-10.22977-10.22977-26.085914-10.22977-36.315684 0s-10.22977 26.085914 0 36.315684L475.684827 512 8.184328 980.011988c-10.22977 10.22977-10.22977 26.085914 0 36.315684 5.114885 5.114885 11.764236 7.672328 17.902098 7.672328s13.298701-2.557443 17.902097-7.672328l468.011988-468.011988 468.011989 468.011988c5.114885 5.114885 11.764236 7.672328 17.902097 7.672328s13.298701-2.557443 17.902098-7.672328c10.22977-10.22977 10.22977-26.085914 0-36.315684L548.316196 512z" fill="#8a8a8a" p-id="6970"></path>
                        </svg>
                    </button>
                    <span class="flex items-center h-6 px-3 text-xs font-semibold text-green-500 bg-green-100 rounded-full">Tips</span>
                    <h4 class="mt-3 text-md font-medium"><b>${name}</b></h4>
                    <p class="mt-3 text-sm text-gray-500">${description}</p>
                    <div class="flex items-center w-full mt-3 text-xs font-medium text-gray-400">
                        <div class="flex items-center">
                            <svg t="1713520227169" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4317" width="16" height="16">
                                <path d="M513.871 21.19c-271.033 0-491.52 220.487-491.52 491.52s220.487 491.52 491.52 491.52 491.52-220.487 491.52-491.52-220.487-491.52-491.52-491.52zM513.871 963.27c-248.436 0-450.56-202.124-450.56-450.56s202.124-450.56 450.56-450.56 450.56 202.124 450.56 450.56-202.124 450.56-450.56 450.56z" fill="#bfbfbf" p-id="4318"></path><path d="M769.516 570.737l-314.669 0.041v-314.491c0-11.264-9.216-20.48-20.48-20.48s-20.48 9.216-20.48 20.48c0 0-0.041 334.739-0.041 334.971 0 11.264 9.216 20.48 20.48 20.48l335.175-0.041c11.264 0 20.48-9.216 20.48-20.48 0.014-11.264-9.202-20.48-20.466-20.48z" fill="#bfbfbf" p-id="4319"></path>
                            </svg>
                            <span class="ml-1 leading-none items-center">${time}</span>
                        </div>
                    </div>
                </div>`;
            htmlContent += text;
        }

        courseInfo.innerHTML = htmlContent;
    }
    catch (error) {
        console.log(error);
    }
}

async function displayCare() {
    const countText = document.getElementById('careCount');
    const courseInfo = document.getElementById('careInfo');

    try {
        let response = await fetch('/getHealthcare');
        let data = await response.json();
        let care = data["care"];
        let count = data["count"];
        countText.innerHTML = `${count}`;
        let htmlContent = '';

        for (let i = 0; i < count; i++) {
            let bid = care[i]["BID"]
            let brand = care[i]["Brand"]
            let type = care[i]["Type"]
            let expire = care[i]["Expire"]
            let description = care[i]["Description"]
            let timeleft = dayjs(expire).diff(dayjs(), 'day');

            let text = `<div class="relative flex flex-col items-start p-4 mt-3 bg-white rounded-lg cursor-pointer bg-opacity-90 group hover:bg-opacity-100" draggable="true">
                    <button class="careDelete absolute top-0 right-0 flex items-center justify-center hidden w-5 h-5 mt-3 mr-2 text-gray-500 rounded hover:bg-gray-200 hover:text-gray-700 group-hover:flex" bid="${bid}">
                        <svg t="1713527777962" class="icon" viewBox="0 0 1025 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6969" width="15" height="15">
                            <path d="M548.316196 512l468.011988-468.011988c10.22977-10.22977 10.22977-26.085914 0-36.315684s-26.085914-10.22977-36.315684 0L512.000511 475.684316 43.988523 8.183816c-10.22977-10.22977-26.085914-10.22977-36.315684 0s-10.22977 26.085914 0 36.315684L475.684827 512 8.184328 980.011988c-10.22977 10.22977-10.22977 26.085914 0 36.315684 5.114885 5.114885 11.764236 7.672328 17.902098 7.672328s13.298701-2.557443 17.902097-7.672328l468.011988-468.011988 468.011989 468.011988c5.114885 5.114885 11.764236 7.672328 17.902097 7.672328s13.298701-2.557443 17.902098-7.672328c10.22977-10.22977 10.22977-26.085914 0-36.315684L548.316196 512z" fill="#8a8a8a" p-id="6970"></path>
                        </svg>
                    </button>
                    <span class="flex items-center h-6 px-3 text-xs font-semibold text-purple-500 bg-purple-100 rounded-full">${brand}</span>
                    <h4 class="mt-3 text-md font-medium"><b>${type}</b></h4>
                    <p class="mt-3 text-sm text-gray-500">${description}</p>
                    <div class="flex items-center w-full mt-3 text-xs font-medium text-gray-400">
                        <div class="flex items-center">
                            <svg t="1713522191388" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5633" width="20" height="20">
                                <path d="M622.9504 76.8H153.6a25.6 25.6 0 0 0-25.6 25.6v819.2a25.6 25.6 0 0 0 25.6 25.6h716.8a25.6 25.6 0 0 0 25.6-25.6V287.7952a25.6 25.6 0 0 0-10.24-20.48L638.3104 81.92a25.6 25.6 0 0 0-15.36-5.12zM614.4 128l230.4 172.5952V896h-665.6v-768H614.4z" fill="#bfbfbf" p-id="5634"></path><path d="M512 307.2a25.6 25.6 0 0 1 25.1904 20.992l0.4096 4.608v204.8a25.6 25.6 0 0 1-50.7904 4.608L486.4 537.6v-204.8A25.6 25.6 0 0 1 512 307.2zM512 614.4a51.2 51.2 0 1 1 0 102.4 51.2 51.2 0 0 1 0-102.4z" fill="#bfbfbf" p-id="5635"></path>
                            </svg>
                            <span class="ml-1 leading-none items-center">保质期至：${expire}</span><span class="ml-2 leading-none items-center">还剩：${timeleft} 天</span>
                        </div>
                        
                    </div>
                </div>`;
            htmlContent += text;
        }

        courseInfo.innerHTML = htmlContent;
    }
    catch (error) {
        console.log(error);
    }
}

async function displayGallery() {
    const countText = document.getElementById('galleryCount');
    const courseInfo = document.getElementById('galleryInfo');

    try {
        let response = await fetch('/getGallery');
        let data = await response.json();
        let gallery = data["gallery"];
        let count = data["count"];
        countText.innerHTML = `${count}`;
        let htmlContent = '';

        for (let i = 0; i < count; i++) {
            let gid = gallery[i]["GID"]
            const address = gallery[i]["Address"];

            let text = `<div class="relative flex flex-col items-start p-4 mt-3 bg-white rounded-lg cursor-pointer bg-opacity-90 group hover:bg-opacity-100" draggable="true">
                    <button class="galleryDelete absolute top-0 right-0 flex items-center justify-center hidden w-5 h-5 mt-3 mr-2 text-gray-500 rounded hover:bg-gray-200 hover:text-gray-700 group-hover:flex" gid="${gid}">
                        <svg t="1713527777962" class="icon" viewBox="0 0 1025 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6969" width="15" height="15">
                            <path d="M548.316196 512l468.011988-468.011988c10.22977-10.22977 10.22977-26.085914 0-36.315684s-26.085914-10.22977-36.315684 0L512.000511 475.684316 43.988523 8.183816c-10.22977-10.22977-26.085914-10.22977-36.315684 0s-10.22977 26.085914 0 36.315684L475.684827 512 8.184328 980.011988c-10.22977 10.22977-10.22977 26.085914 0 36.315684 5.114885 5.114885 11.764236 7.672328 17.902098 7.672328s13.298701-2.557443 17.902097-7.672328l468.011988-468.011988 468.011989 468.011988c5.114885 5.114885 11.764236 7.672328 17.902097 7.672328s13.298701-2.557443 17.902098-7.672328c10.22977-10.22977 10.22977-26.085914 0-36.315684L548.316196 512z" fill="#8a8a8a" p-id="6970"></path>
                        </svg>
                    </button>
                    <div class="grid gap-4 col-start-1 col-end-3 row-start-1 ">
						<img src="${address}" alt="" class="w-full object-cover rounded-lg sm:h-52 sm:col-span-2 lg:col-span-full" loading="lazy">
					</div>
                </div>`;
            htmlContent += text;
        }

        courseInfo.innerHTML = htmlContent;
    }
    catch (error) {
        console.log(error);
    }
}

let onCount = 0;
async function displayStatus() {
    weatherToggle = document.getElementById('weatherToggle');
    newsToggle = document.getElementById('newsToggle');
    courseToggle = document.getElementById('courseToggle');
    scheduleToggle = document.getElementById('scheduleToggle');
    tipsToggle = document.getElementById('tipsToggle');
    careToggle = document.getElementById('careToggle');
    galleryToggle = document.getElementById('galleryToggle');

    try {
        const response = await fetch('/getStatus')
        const status = await response.json();
        if (status["Weather"] == 1) {
            weatherToggle.checked = true;
        }
        if (status["News"] == 1) {
            newsToggle.checked = true;
            onCount++;
        }
        if (status["Course"] == 1) {
            courseToggle.checked = true;
            onCount++;
        }
        if (status["Schedule"] == 1) {
            scheduleToggle.checked = true;
            onCount++;
        }
        if (status["Tips"] == 1) {
            tipsToggle.checked = true;
            onCount++;
        }
        if (status["Care"] == 1) {
            careToggle.checked = true;
            onCount++;
        }
        if (status["Gallery"] == 1) {
            galleryToggle.checked = true;
            onCount++;
        }
        console.log("Open bottoms: " + onCount);
    }
    catch (error) {
        console.log(error);
    }
}

// Toast
let toastIntervalId;

async function showToast(message, duration = 3000) {
    const toast = document.getElementById('toast');
    const toastBody = document.getElementById('toast-body');
    const toastProgress = document.getElementById('toast-progress');
    const closeButton = document.querySelector('.galleryModalClose');

    // 如果上一个提示框还没结束，则直接覆盖当前信息，并重置进度条
    clearInterval(toastIntervalId);
    toastBody.textContent = message;
    toastProgress.style.width = '0%';

    // 显示提示框
    toast.classList.remove('opacity-0');
    toast.classList.add('opacity-100');

    // 开始递减进度条
    let start = Date.now();
    toastIntervalId = setInterval(() => {
        let timePassed = Date.now() - start;
        let progress = Math.max(0, 100 - (timePassed / duration) * 100);
        toastProgress.style.width = progress + '%';

        // 当进度条完成时，关闭提示框
        if (timePassed >= duration) {
            clearInterval(toastIntervalId);
            // 隐藏提示框
            toast.classList.remove('opacity-100');
            toast.classList.add('opacity-0');
            // 移除提示信息
            setTimeout(() => {
                toastBody.textContent = '';
            }, 500); // 等待过渡动画完成
        }
    }, 10);

    // 点击关闭按钮隐藏提示框
    closeButton.addEventListener('click', () => {
        clearInterval(toastIntervalId);
        toast.classList.remove('opacity-100');
        toast.classList.add('opacity-0');
    });
}

// Switch Bottom Logic
async function weatherBottomLogic(){
    const toggle = document.getElementById('weatherToggle');

    toggle.addEventListener('change', async function() {
        if (toggle.checked) {
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Weather", state: 1})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('天气模块已开启');
                console.log('weatherToggle is on');
            }).catch(error => {
                console.error('Error:', error);
                showToast('天气模块开启失败' + error);
            })
        } else {
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Weather", state: 0})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('天气模块已关闭');
                console.log('weatherToggle is off');
            }).catch(error => {
                console.error('Error:', error);
                showToast('天气模块关闭失败' + error);
            })
        }
    });
}

async function newsBottomLogic(){
    const toggle = document.getElementById('newsToggle');

    toggle.addEventListener('change', async function() {
        if (toggle.checked) {
            if (onCount + 1 > 2){
                showToast('除天气外最多只能开启两个模块');
                toggle.checked = false;
                return;
            }
            onCount++;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "News", state: 1})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('新闻模块已开启');
                console.log('newsToggle is on');
            }).catch(error => {
                console.error('Error:', error);
                showToast('新闻模块开启失败' + error);
            })

        } else {
            onCount--;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "News", state: 0})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('新闻模块已关闭');
                console.log('newsToggle is off');
            }).catch(error => {
                console.error('Error:', error);
                showToast('新闻模块关闭失败' + error);
            })
        }
    });
}

async function courseBottomLogic(){
    const toggle = document.getElementById('courseToggle');

    toggle.addEventListener('change', async function() {
        if (toggle.checked) {
            if (onCount + 1 >= 2){
                showToast('除了天气外最多只能开启两个模块');
                toggle.checked = false;
                return;
            }
            onCount++;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Course", state: 1})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('课程模块已开启');
                console.log('courseToggle is on');
            }).catch(error => {
                console.error('Error:', error);
                showToast('课程模块开启失败' + error);
            })
            
        } else {
            onCount--;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Course", state: 0})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('课程模块已关闭');
                console.log('courseToggle is off');
            }).catch(error => {
                console.error('Error:', error);
                showToast('课程模块关闭失败' + error);
            })
        }
    });
}

async function scheduleBottomLogic(){
    const toggle = document.getElementById('scheduleToggle');

    toggle.addEventListener('change', async function() {
        if (toggle.checked) {
            if (onCount + 1 > 2){
                showToast('除了课程模块最多只能开启两个模块');
                toggle.checked = false;
                return;
            }
            onCount++;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Schedule", state: 1})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('日程模块已开启');
                console.log('scheduleToggle is on');
            }).catch(error => {
                console.error('Error:', error);
                showToast('日程模块开启失败' + error);
            })
        } else {
            onCount--;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Schedule", state: 0})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('日程模块已关闭');
                console.log('scheduleToggle is off');
            }).catch(error => {
                console.error('Error:', error);
                showToast('日程模块关闭失败' + error);
            })
        }
    });
}

async function tipsBottomLogic(){
    const toggle = document.getElementById('tipsToggle');

    toggle.addEventListener('change', async function() {
        if (toggle.checked) {
            if (onCount + 1 > 2){
                showToast('除天气外最多只能开启两个模块');
                toggle.checked = false;
                return;
            }
            onCount++;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Tips", state: 1})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('备忘录模块已开启');
                console.log('tipsToggle is on');
            }).catch(error => {
                console.error('Error:', error);
                showToast('备忘录模块开启失败' + error);
            })
        } else {
            onCount--;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Tips", state: 0})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('备忘录模块已关闭');
                console.log('tipsToggle is off');
            }).catch(error => {
                console.error('Error:', error);
                showToast('备忘录模块关闭失败' + error);
            })
        }
    });
}

async function careBottomLogic(){
    const toggle = document.getElementById('careToggle');

    toggle.addEventListener('change', async function() {
        if (toggle.checked) {
            if (onCount + 1 > 2){
                showToast('除天气外最多只能开启两个模块');
                toggle.checked = false;
                return;
            }
            onCount++;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Care", state: 1})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('个人护理产品模块已开启');
                console.log('careToggle is on');
            }).catch(error => {
                console.error('Error:', error);
                showToast('个人护理产品模块开启失败' + error);
            })
        } else {
            onCount--;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Care", state: 0})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('个人护理产品模块已关闭');
                console.log('careToggle is off');
            }).catch(error => {
                console.error('Error:', error);
                showToast('个人护理产品模块关闭失败' + error);
            })
        }
    });
}

async function galleryBottomLogic(){
    const toggle = document.getElementById('galleryToggle');

    toggle.addEventListener('change', async function() {
        if (toggle.checked) {
            if (onCount + 1 > 2){
                showToast('除天气外最多只能开启两个模块');
                toggle.checked = false;
                return;
            }
            onCount++;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Gallery", state: 1})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('相册模块已开启');
                console.log('galleryToggle is on');
            }).catch(error => {
                console.error('Error:', error);
                showToast('相册模块开启失败' + error);
            })
        } else {
            onCount--;
            await fetch('/changeStatus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({item: "Gallery", state: 0})
            }).then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                showToast('相册模块已关闭');
                console.log('galleryToggle is off');
            }).catch(error => {
                console.error('Error:', error);
                showToast('相册模块关闭失败' + error);
            })
        }
    });
}

// Add bottoms logic
async function addCourse() {
    // 获取模态和按钮元素
    const modal = document.getElementById('courseModal');
    const addButton = document.getElementById('addCourse');
    const closeModalButtons = document.querySelectorAll('.courseModalClose');
    const title = document.getElementById('Coursetitle');
    const description = document.getElementById('Coursedescription');
    const week = document.getElementById('Courseweek');
    const time = document.getElementById('Coursetime');
    const location = document.getElementById('Courselocation');

    // 显示模态的函数
    function showModal() {
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modal.classList.add('opacity-100');
        title.focus(); // 自动聚焦到输入框
    }

    // 隐藏模态的函数
    function hideModal() {
        modal.classList.remove('opacity-100');
        modal.classList.add('opacity-0', 'pointer-events-none');
    }

    // 点击按钮显示模态
    addButton.addEventListener('click', showModal);

    // 点击关闭按钮或背景隐藏模态
    closeModalButtons.forEach(button => {
        button.addEventListener('click', hideModal);
    });

    // 按下Esc键也可以关闭模态
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            hideModal();
        }
    });

    // 处理确认按钮点击事件
    const confirmButton = document.getElementById('courseModalConfirm');
    confirmButton.addEventListener('click', async() => {
        if (title.value === '') {
            showToast('请输入标题');
            return;
        }
        if (week.value === '') {
            showToast('请输入星期');
            return;
        }
        if (time.value === '') {
            showToast('请输入时间');
            return;
        }
        const userInput = {
            title: title.value,
            description: description.value,
            week: week.value,
            time: time.value,
            location: location.value
        }
        console.log('用户输入:', userInput);
        
        try {
            await fetch('/addCourse', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(userInput),
            }).then(async response => {
                if (!response.ok) {
                    throw Error(`HTTP error! status: ${response.status}`);
                }
                showToast('添加课程成功');
                console.log('添加课程成功');
                title.value = '';
                description.value = '';
                week.value = '';
                time.value = '';
                location.value = '';
                await displayCourses();
                await deleteCourseLogic();
            }).catch(error => {
                showToast(`添加课程失败: ${error.message}`);
                throw error;
            });
        }
        catch (error) {
            console.log(`Request failed: ${error.message}`);
        }
        hideModal(); // 隐藏模态
    });

    // 阻止模态内容点击时关闭模态
    document.getElementById('courseModalContainer').addEventListener('click', (e) => {
        e.stopPropagation();
    });
}

async function addSchedule() {
    // 获取模态和按钮元素
    const modal = document.getElementById('scheduleModal');
    const addButton = document.getElementById('addSchedule');
    const closeModalButtons = document.querySelectorAll('.scheduleModalClose');
    const title = document.getElementById('Scheduletitle');
    const description = document.getElementById('Scheduledescription');
    const time = document.getElementById('Scheduletime');
    const location = document.getElementById('Schedulelocation');

    // 显示模态的函数
    function showModal() {
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modal.classList.add('opacity-100');
        title.focus(); // 自动聚焦到输入框
    }

    // 隐藏模态的函数
    function hideModal() {
        modal.classList.remove('opacity-100');
        modal.classList.add('opacity-0', 'pointer-events-none');
    }

    // 点击按钮显示模态
    addButton.addEventListener('click', showModal);

    // 点击关闭按钮或背景隐藏模态
    closeModalButtons.forEach(button => {
        button.addEventListener('click', hideModal);
    });

    // 按下Esc键也可以关闭模态
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            hideModal();
        }
    });

    // 处理确认按钮点击事件
    const confirmButton = document.getElementById('scheduleModalConfirm');
    confirmButton.addEventListener('click', async() => {
        if (title.value === '') {
            showToast('请输入标题');
            return;
        }
        if (time.value === '') {
            showToast('请输入时间');
            return;
        }
        const userInput = {
            title: title.value,
            description: description.value,
            time: time.value,
            location: location.value
        }
        console.log('用户输入:', userInput);
        
        await fetch('/addSchedule', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userInput),
        })
        .then(async response => {
            if (!response.ok) {
                throw Error(`HTTP error! status: ${response.status}`);
            }
            showToast('添加日程成功');
            console.log('添加日程成功');
            title.value = '';
            description.value = '';
            time.value = '';
            location.value = '';
            await displaySchedule();
            await deleteScheduleLogic();
        })
        .catch(error => {
            showToast(`添加日程失败: ${error.message}`);
            console.log(`Request failed: ${error.message}`);
            throw error;
        })

        hideModal(); // 隐藏模态
    });

    // 阻止模态内容点击时关闭模态
    const scheduleModalContainer = document.getElementById('scheduleModalContainer');
    scheduleModalContainer.addEventListener('click', (e) => {
        e.stopPropagation();
    });
}

async function addTips() {
    // 获取模态和按钮元素
    const modal = document.getElementById('tipsModal');
    const addButton = document.getElementById('addTips');
    const closeModalButtons = document.querySelectorAll('.tipsModalClose');
    const title = document.getElementById('tipsTitle');
    const description = document.getElementById('tipsContent');

    // 显示模态的函数
    function showModal() {
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modal.classList.add('opacity-100');
        title.focus(); // 自动聚焦到输入框
    }

    // 隐藏模态的函数
    function hideModal() {
        modal.classList.remove('opacity-100');
        modal.classList.add('opacity-0', 'pointer-events-none');
    }

    // 点击按钮显示模态
    addButton.addEventListener('click', showModal);

    // 点击关闭按钮或背景隐藏模态
    closeModalButtons.forEach(button => {
        button.addEventListener('click', hideModal);
    });

    // 按下Esc键也可以关闭模态
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            hideModal();
        }
    });

    // 处理确认按钮点击事件
    const confirmButton = document.getElementById('tipsModalConfirm');
    confirmButton.addEventListener('click', async() => {
        if (title.value === '') {
            showToast('请输入标题');
            return;
        }
        if (description.value === '') {
            showToast('请输入内容');
            return;
        }
    
        const published = dayjs().format('YYYY-MM-DD HH:mm:ss');
        const userInput = {
            title: title.value,
            description: description.value,
            published: published
        }
        console.log('用户输入:', userInput);
        await fetch('/addTips', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userInput),
        })
        .then(async response => {
            if (!response.ok) {
                throw Error(`HTTP error! status: ${response.status}`);
            }
            showToast('添加备忘录成功');
            console.log('添加备忘录成功');
            title.value = '';
            description.value = '';
            await displayTips();
            await deleteTipsLogic();
        })
        .catch(error => {
            showToast(`添加备忘录失败: ${error.message}`);
            console.log(`Request failed: ${error.message}`);
            throw error;
        })
        hideModal(); // 隐藏模态
    });

    // 阻止模态内容点击时关闭模态
    const tipsModalContainer = document.getElementById('tipsModalContainer');
    tipsModalContainer.addEventListener('click', (e) => {
        e.stopPropagation();
    });
}

async function addCare() {
    // 获取模态和按钮元素
    const modal = document.getElementById('careModal');
    const addButton = document.getElementById('addCare');
    const closeModalButtons = document.querySelectorAll('.careModalClose');
    const brand = document.getElementById('careBrand');
    const type = document.getElementById('careType');
    const expire = document.getElementById('careExpire');
    const description = document.getElementById('careDescription');

    // 显示模态的函数
    function showModal() {
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modal.classList.add('opacity-100');
        brand.focus(); // 自动聚焦到输入框
    }

    // 隐藏模态的函数
    function hideModal() {
        modal.classList.remove('opacity-100');
        modal.classList.add('opacity-0', 'pointer-events-none');
    }

    // 点击按钮显示模态
    addButton.addEventListener('click', showModal);

    // 点击关闭按钮或背景隐藏模态
    closeModalButtons.forEach(button => {
        button.addEventListener('click', hideModal);
    });

    // 按下Esc键也可以关闭模态
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            hideModal();
        }
    });

    // 处理确认按钮点击事件
    const confirmButton = document.getElementById('careModalConfirm');
    confirmButton.addEventListener('click', async() => {
        if (brand.value === '') {
            showToast('请输入品牌');
            return;
        }
        if (type.value === '') {
            showToast('请输入产品类型');
            return;
        }
        if (expire.value === '') {
            showToast('请输入过期时间');
            return;
        }
        const userInput = {
            brand: brand.value,
            type: type.value,
            expire: expire.value,
            description: description.value
        }
        console.log('用户输入:', userInput);
        await fetch('/addHealthcare', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userInput)
        })
        .then(async response => {
            if (!response.ok) {
                throw Error(`HTTP error! status: ${response.status}`);
            }
            showToast('添加个人护理产品成功');
            console.log('添加个人护理产品成功');
            brand.value = '';
            type.value = '';
            expire.value = '';
            description.value = '';
            await displayCare();
            await deleteCareLogic();
        })
        .catch(error => {
            showToast(`添加个人护理产品失败: ${error.message}`);
            console.log(`Request failed: ${error.message}`);
            throw error;
        })
        hideModal(); // 隐藏模态
    });

    // 阻止模态内容点击时关闭模态
    const careModalContainer = document.getElementById('careModalContainer');
    careModalContainer.addEventListener('click', (e) => {
        e.stopPropagation();
    });
}

async function addGallery() {
    // 获取模态窗口、触发按钮和关闭按钮的DOM元素
    const modal = document.getElementById('galleryModal');
    const addButton = document.getElementById('addGallery');
    const closeModalButtons = document.querySelectorAll('.galleryModalClose');
    const fileInput = document.querySelector('.file-upload-container input[type="file"]');
    const uploadLabel = document.querySelector('.upload-label');
    const confirmButton = document.getElementById('galleryModalConfirm');
    const filePreview = document.getElementById('filePreview');
    const fileUploadContainer = document.querySelector('.file-upload-container');
    const clearButton = document.getElementById('clearButton');

    // 显示模态窗口
    function showModal() {
        modal.classList.remove('opacity-0', 'pointer-events-none');
        modal.classList.add('opacity-100');
    }

    // 隐藏模态窗口
    function hideModal() {
        modal.classList.remove('opacity-100');
        modal.classList.add('opacity-0', 'pointer-events-none');
    }

    // 点击按钮显示模态窗口
    addButton.addEventListener('click', showModal);

    // 点击关闭按钮或背景隐藏模态窗口
    closeModalButtons.forEach(button => {
        button.addEventListener('click', hideModal);
    });

    // 按下Esc键也可以关闭模态窗口
    window.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            hideModal();
        }
    });

    // 显示文件预览的函数
    function showFilePreview(file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            filePreview.src = e.target.result;
            filePreview.classList.remove('hidden');
        };
        reader.readAsDataURL(file);
    }

    // 清除选择的文件和预览
    function clearFile() {
        fileInput.value = ''; // 清除input的文件
        filePreviewContainer.innerHTML = ''; // 清除图片预览容器的内容
        filePreviewContainer.style.display = 'none'; // 隐藏图片预览容器
        fileUploadContainer.style.display = 'block'; // 显示文件上传容器
    }

    // 显示文件预览
    function showFilePreview(file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = document.createElement('img');
            img.src = e.target.result;
            img.style.maxWidth = '100%'; // 设置最大宽度，确保预览图片不会太大
            img.classList.add('mx-auto'); // 居中图片
            filePreviewContainer.appendChild(img); // 将预览图片添加到容器中
            filePreviewContainer.style.display = 'block'; // 显示图片预览容器
            fileUploadContainer.style.display = 'none'; // 隐藏文件上传容器
        };
        reader.readAsDataURL(file);
    }

    async function uploadFile(file) {
        const formData = new FormData();
        formData.append('file', file);
        if (!file) {
            showToast('文件列表为空');
            return;
        }

        try {
            const response = await fetch('/addGallery', {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            showToast('上传成功');
            console.log('上传成功', result);
            clearFile();
            hideModal();
            await displayGallery();
            await deleteGalleryLogic();
        } catch (error) {
            console.error('Error uploading file:', error);
            showToast('上传失败' + error);
        }
    }

    // 修改拖拽和文件选择事件处理函数，以显示预览而不是立即上传
    uploadLabel.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadLabel.classList.add('bg-blue-500', 'text-white');
    });

    uploadLabel.addEventListener('dragleave', (e) => {
        e.preventDefault();
        uploadLabel.classList.remove('bg-blue-500', 'text-white');
    });

    uploadLabel.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadLabel.classList.remove('bg-blue-500', 'text-white');
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            showFilePreview(files[0]); // 显示文件预览
        }
    });

    fileInput.addEventListener('change', () => {
        const files = fileInput.files;
        if (files.length > 0) {
            showFilePreview(files[0]); // 显示文件预览
        }
    });

    // 修改确认按钮点击事件处理函数，点击时才上传文件
    confirmButton.addEventListener('click', () => {
        const files = fileInput.files;
        if (files.length > 0) {
            uploadFile(files[0]); // 上传文件
        } else {
            console.log('No file selected.');
        }
    });

    // 为清除按钮添加点击事件处理函数
    clearButton.addEventListener('click', clearFile);


    // 阻止模态内容点击时关闭模态窗口
    const galleryModalContainer = document.getElementById('galleryModalContainer');
    galleryModalContainer.addEventListener('click', (e) => {
        e.stopPropagation();
    });
}

// Delete bottoms logic
async function deleteCourseLogic() {
    const deleteButtons = document.querySelectorAll('.courseDelete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', async function() {
            const cid = this.getAttribute('cid');
            
            const data = { 
                cid: cid
            };

            await deleteCourse(data);
        });
    });

    async function deleteCourse(data) {
        try {
            const response = await fetch('/deleteCourse', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            showToast('删除成功');
            console.log('Delete successful.');
            await displayCourses();
            await deleteCourseLogic();
        } catch (error) {
            
            console.error('Error deleting:', error);
        }
    }
}

async function deleteScheduleLogic() {
    const deleteButtons = document.querySelectorAll('.scheduleDelete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', async function() {
            const sid = this.getAttribute('sid');
            
            const data = { 
                sid: sid
            };

            await deleteSchedule(data);
        });
    });

    async function deleteSchedule(data) {
        try {
            const response = await fetch('/deleteSchedule', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            showToast('删除成功');
            console.log('Delete successful.');
            await displaySchedule();
            await deleteScheduleLogic();
        } catch (error) {
            
            console.error('Error deleting:', error);
        }
    }
}

async function deleteTipsLogic() {
    const deleteButtons = document.querySelectorAll('.tipsDelete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', async function() {
            const tid = this.getAttribute('tid');
            
            const data = { 
                tid: tid
            };

            await deleteTips(data);
        });
    });

    async function deleteTips(data) {
        try {
            const response = await fetch('/deleteTips', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            showToast('删除成功');
            console.log('Delete successful.');
            await displayTips();
            await deleteTipsLogic();
        } catch (error) {
            
            console.error('Error deleting:', error);
        }
    }
}

async function deleteCareLogic() {
    const deleteButtons = document.querySelectorAll('.careDelete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', async function() {
            const bid = this.getAttribute('bid');
            
            const data = { 
                bid: bid
            };

            await deleteCare(data);
        });
    });

    async function deleteCare(data) {
        try {
            const response = await fetch('/deleteCare', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            showToast('删除成功');
            console.log('Delete successful.');
            await displayCare();
            await deleteCareLogic();
        } catch (error) {
            
            console.error('Error deleting:', error);
        }
    }
}

async function deleteGalleryLogic() {
    const deleteButtons = document.querySelectorAll('.galleryDelete');

    deleteButtons.forEach(button => {
        button.addEventListener('click', async function() {
            const gid = this.getAttribute('gid');
            
            const data = { 
                gid: gid
            };

            await deleteGallery(data);
            await deleteGalleryLogic();
        });
    });

    async function deleteGallery(data) {
        try {
            const response = await fetch('/deleteGallery', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            showToast('删除成功');
            console.log('Delete successful.');
            await displayGallery();
        } catch (error) {
            
            console.error('Error deleting:', error);
        }
    }
}

// Initial start
async function initialStart() {
    await displayCourses();
    await displaySchedule();
    await displayTips();
    await displayCare();
    await displayGallery();
    await displayStatus();

    await weatherBottomLogic();
    await newsBottomLogic();
    await courseBottomLogic();
    await scheduleBottomLogic();
    await tipsBottomLogic();
    await careBottomLogic();
    await galleryBottomLogic();

    await addCourse();
    await addSchedule();
    await addTips();
    await addCare();
    await addGallery();

    await deleteCourseLogic();
    await deleteScheduleLogic();
    await deleteTipsLogic();
    await deleteCareLogic();
    await deleteGalleryLogic();
}

window.onload = initialStart;
