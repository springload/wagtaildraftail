import WagtailModalSource from './WagtailModalSource';

const $ = global.jQuery;

class WagtailImageSource extends WagtailModalSource {
    constructor(props) {
        super(props);
        this.parseData = this.parseData.bind(this);
    }

    parseData(imageData) {
        this.onConfirmAtomicBlock(Object.assign({}, imageData, {
            src: imageData.preview.url,
        }));
    }

    componentDidMount() {
        const imageChooser = global.chooserUrls.imageChooser;
        $(document.body).on('hidden.bs.modal', this.onClose);

        global.ModalWorkflow({
            url: imageChooser,
            responses: {
                imageChosen: this.parseData,
            },
        });
    }
}

export default WagtailImageSource;
