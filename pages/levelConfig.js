export default function LevelConfig (id, name, definition) {
        this.name = name;
        this.definition = definition;

        this.id = id;
}


const levelDefinitions = require('./levels.json');
export const defaultLevels = levelDefinitions.map(({name, definition}, index) => new LevelConfig(index, name, definition));
