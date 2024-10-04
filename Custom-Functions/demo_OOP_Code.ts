// This is a demo version of the User class for my project.
// The original project is in a private Git repository, and all specific imports have been removed.

export class User {
  constructor(
    private user_id: number,
    private access_token: string = "",
    public projects: Project[] = [],
    public user_name: string = "Default Name",
    public user_mail: string = "default@example.com",
    public isActive: boolean = true,
    public job: string = "Default Job", // Example: "architect", "designer"
    public country: string = "Default Country",
    public city: string = "",
    public logiciels: string[] = ["Software A", "Software B", "Software C"],
    public langue: string = "FR",
    public relations: Relation[] = [],
    public subscriptionType: SubscriptionType = SubscriptionType.FREE,
    public startSubscription: string = "2024-01-01",
    public endSubscription: string = "2024-12-31",
    public lots: Lot[] = [],
    public dark_mode: boolean = true,
    public uniteList: any = {},
    public code_seperator: string = "|",
    public key_words: string = "",
    public list_of_code_seperator: string[] = ["|", " ", "-", "_", ".", ";"],
    public user_relations: number[] = [],
    public image: string = "",
    public secret_code: string = "",
    public project_visited: boolean = false,
    public messages: Message[] = [],
    public messages_visited: boolean = false,
    public all_user_friends: User[] = [],
    public visitedUsersIds: number[] = [],
    public all_users_unites = {},
    public pdfParams: PdfParams = new PdfParams(),
    public selected_unit_system: boolean = false,
    public bio: string = "",
    public company: string = "",
    public company_location: string = ""
  ) {}

  // Verify the user's password
  public async verifPassWord(_password: string): Promise<boolean> {
    try {
      const result = await axios.post(`${prefix_url}/verifyPassword`, {
        token: this.access_token,
        user_password: _password,
      });
      return result.data && result.data.passwordMatch;
    } catch (error) {
      console.error("Error verifying password:", error);
      return false;
    }
  }

  // Store user data in local storage
  static store_in_local_user(user: User) {
    const userJson = JSON.stringify(user); // Convert user to JSON
    localStorage.setItem("user", userJson); // Store in local storage
  }

  // Retrieve user data from local storage
  static get_user_from_local_storage(): User | undefined {
    const retrievedUserJson = localStorage.getItem("user");
    if (retrievedUserJson) {
      try {
        const parsedUserObj = JSON.parse(retrievedUserJson);
        return User.fromObject(parsedUserObj); // Convert back to User instance
      } catch (error) {
        console.error("Error parsing user JSON from local storage", error);
        return undefined;
      }
    }
    return undefined; // Return undefined if not found
  }

  // Method to get user details
  public async getUser(
    _user_name: string,
    user_password: string,
    setData: any
  ): Promise<{ userValid: boolean; message: string; user: User }> {
    const retrievedUserJson = localStorage.getItem("user");
    if (retrievedUserJson) {
      const parsedUserObj = JSON.parse(retrievedUserJson);
      const user = User.fromObject(parsedUserObj); // Convert back to User instance
      return { userValid: true, message: "", user };
    }

    const requestBody = {
      user_name: _user_name,
      user_password,
    };
    try {
      const result = await axios.post(`${prefix_url}/login`, requestBody);
      if (result.data.result) {
        const {
          user_id,
          token,
          user_name,
          user_mail,
          job,
          country,
          city,
          logiciels,
          langue,
          userValid,
          subscriptionType,
          startSubscription,
          endSubscription,
          dark_mode,
          unite_list,
          code_seperator,
          key_words,
          user_relations,
          image,
          secret_code,
          pdf_params,
          selected_unit_system,
          bio,
          company,
          company_location,
        } = result.data.result;

        let user: User;
        this.setUserToken(token); // Set token
        this.setUserId(user_id); // Set user ID

        if (userValid) {
          user = new User(
            user_id,
            token,
            [],
            user_name,
            user_mail,
            true,
            job,
            country,
            city,
            logiciels,
            langue,
            [],
            subscriptionType,
            startSubscription,
            endSubscription,
            [],
            true,
            unite_list,
            code_seperator,
            key_words
          );
          user.pdfParams = new PdfParams(
            pdf_params?.font_type,
            pdf_params?.isBold
          ); // Set PDF parameters
          user.user_relations = user_relations; // Set user relations
          user.image = image; // Set user image
          user.secret_code = secret_code; // Set secret code
          user.selected_unit_system = selected_unit_system; // Set unit system
          user.bio = bio; // Set bio
          user.company = company; // Set company name
          user.company_location = company_location; // Set company location
        } else {
          user = new User(user_id, token); // Create user with basic info
        }

        User.store_in_local_user(user); // Store user in local storage
        return { userValid, message: "", user }; // Return user info
      } else {
        throw new Error("Failed to retrieve user Data from the response");
      }
    } catch (error) {
      console.error("Error getting user data from the database:", error);
      throw new Error("Failed to get user data from the database");
    }
  }

  // Check user access based on subscription type
  public hasAccess(feature: string): boolean {
    switch (this.subscriptionType) {
      case SubscriptionType.FREE:
        return feature === "BasicFeature";
      case SubscriptionType.BASIC:
        return feature === "BasicFeature" || feature === "IntermediateFeature";
      case SubscriptionType.PREMIUM:
        return true; // Premium users have access to all features
      default:
        return false;
    }
  }

  // Check if the subscription is active
  public isSubscriptionActive(): boolean {
    const currentDate = new Date();
    const endDate = new Date(this.endSubscription);
    return currentDate <= endDate; // Check if current date is less than or equal to end date
  }

  // Renew subscription with a new end date
  public renewSubscription(newEndDate: string): void {
    this.endSubscription = newEndDate; // Set new end date
  }

  // Add a new project
  public async addProject(
    project: Project,
    trancheName: string,
    setData: any
  ): Promise<Project[]> {
    // Define inner function to add project to database
    const addProjectToDB = async (): Promise<number> => {
      const {
        project_name,
        address,
        project_creation_date,
        client_name,
        last_update,
      } = project;

      const requestBody = {
        token: this.getUserToken(),
        variables: {
          project_name,
          project_address: address,
          project_creation_date: project_creation_date,
          last_update,
          client_name,
        },
        tableName: "user_project",
      };

      try {
        const result = await axios.post(
          `${prefix_url}/insertSingleRow`,
          requestBody
        );
        if (result.data.result && result.data.result.insertID) {
          return result.data.result.insertID; // Return new project ID
        } else {
          throw new Error(
            "Failed to retrieve new project ID from the response"
          );
        }
      } catch (error) {
        console.error("Error adding project to the database:", error);
        throw new Error("Failed to add project to the database");
      }
    };

    // Handle the addition of the project
    try {
      const insertID = await addProjectToDB(); // Add project to the database
      project.id = insertID; // Set project ID
      // Further processing for project can be done here
      this.projects.push(project); // Add project to user's projects
      return this.projects; // Return updated project list
    } catch (error) {
      console.error("Error in addProject method:", error);
      throw error;
    }
  }
}
