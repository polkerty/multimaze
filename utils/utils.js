// https://stackoverflow.com/questions/1322732/convert-seconds-to-hh-mm-ss-with-javascript
export const toHHMMSS = (secs) => {
    let sec_num = parseInt(secs, 10)
    let hours = Math.floor(sec_num / 3600)
    let minutes = Math.floor(sec_num / 60) % 60
    let seconds = sec_num % 60

    return [hours, minutes, seconds]
        .map(v => v < 10 ? "0" + v : v)
        .filter((v, i) => v !== "00" || i > 0)
        .join(":")
}

