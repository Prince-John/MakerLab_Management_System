import { store } from "react-notifications-component";

const animation = {
  animationIn: ["animate__animated", "animate__fadeIn"],
  animationOut: ["animate__animated", "animate__fadeOut"],
  dismiss: {
    duration: 2500,
    onScreen: true,
  },
};
export const logMessage = (message: string) => {
  store.addNotification({
    message,
    type: "success",
    insert: "top",
    container: "top-right",
    ...animation,
  });
};

export const userNotRegistered = () => {
  store.addNotification({
    title: "User Not Registered",
    message: "Please Register",
    type: "warning",
    insert: "top",
    container: "top-right",
    ...animation,
  });
};

export const registrationFailed = () => {
  store.addNotification({
    title: "Registration Failed",
    message: "Error",
    type: "danger",
    insert: "top",
    container: "top-center",
    ...animation,
  });
};

export const itemSubmitted = () => {
  store.addNotification({
    title: "Items Submitted",
    message: "Thank you, see you soon",
    type: "success",
    insert: "top",
    container: "top-right",
    ...animation,
  });
};
