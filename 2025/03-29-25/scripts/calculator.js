

const maxSquat = (squat, reps) => {
    console.log(`You squat ${squat} for ${reps}`)

    const squatMax = squat / (1.0278 - (0.0278 * reps))
    return squatMax;
}

export { maxSquat };