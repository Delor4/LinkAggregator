import Axios from "axios"


/* API ENDPOINTS */
class Api {
  constructor() {
    this.api = Axios.create({
      //baseURL: apiHost,
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      }
    });
  }

  /* METHODS */
  get = async function (...args){
    return await this.api.get.apply(this.api, args).then(this.getData).catch(this.errorHandle);
  }
  post = async function (...args){
    return await this.api.post.apply(this.api, args).then(this.getData).catch(this.errorHandle);
  }
  put = async function (...args){
    return await this.api.put.apply(this.api, args).then(this.getData).catch(this.errorHandle);
  }
  delete = async function (...args){
    return await this.api.delete.apply(this.api, args).then(this.getData).catch(this.errorHandle);
  }
  /* response handling */
  getData = function (response) {
    console.log(response.config.method, response.config.url, "->", response.status)
    return response.data;
  }

  errorHandle = function (error) {
    console.log('Http error: ', error);

    //return Promise.reject(error);
  }
  /* CARD */
  getCards = async function () {
    return await this.get("/api/cards");
  }
  createCard = async function (card) {
    return await this.post("/api/cards", card);
  }
  updateCard = async function (card) {
    return await this.put("/api/cards/" + card.id, card);
  }
  deleteCard = async function (id) {
    return await this.delete("/api/cards/" + id);
  }
  /* LINK */
  createLink = async function (link) {
    return await this.post("/api/links", link);
  }
  updateLink = async function (link) {
    return await this.put("/api/links/" + link.id, link);
  }
  deleteLink = async function (id) {
    return await this.delete("/api/links/" + id);
  }
  /* TAG */
  getTags = async function () {
    return await this.get("/api/tags");
  }
  createTag = async function (tag) {
    return await this.post("/api/tags", tag);
  }
  updateTag = async function (tag) {
    return await this.put("/api/tags/" + tag.id, tag);
  }
  deleteTag = async function (id) {
    return await this.delete("/api/tags/" + id);
  }
  /* CARD TAGS */
  getCardTags = async function (card_id) {
    return await this.get("/api/cards/" + card_id + "/tags");
  }
  createCardTag = async function (card_id, tag_id) {
    return await this.post("/api/cards/" + card_id + "/tags", { 'tag_id': tag_id });
  }
  deleteCardTag = async function (card_id, tag_id) {
    return await this.delete("/api/cards/" + card_id + "/tags/" + tag_id);
  }
}

const api = new Api()

export default api
