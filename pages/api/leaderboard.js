// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

export default async (req, res) => {

    // We've got a payload

    const payload = JSON.parse(req.body);

    const ip = req.headers['x-forwarded-for'] || null;
    res.statusCode = 200;
    if (process.env.LEADERBOARD_ENDPOINT) {
        payload.ip = ip;
        console.log(payload);
        console.log(process.env.SAVE_ENDPOINT);
        const leaderboard = await fetch(process.env.LEADERBOARD_ENDPOINT, {
            method: 'POST',
            body: JSON.stringify(payload)
        }).then(x => x.json())

        res.json(leaderboard)

        console.log("Leaderboard fetch results: ", leaderboard);
    } else {
        res.json([]);

    }

}
