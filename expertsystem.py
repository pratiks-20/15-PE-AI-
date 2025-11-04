
def diagnose_crop():
    print("🌾 Welcome to the Crop Disease Expert System 🌾")
    print("Answer the following questions with 'yes' or 'no'.\n")

    crop = input("Enter your crop name (e.g., rice, wheat, maize, sugarcane): ").lower()
    yellow_leaves = input("Are the leaves turning yellow? ").lower()
    brown_spots = input("Do you see brown spots on leaves? ").lower()
    white_patches = input("Do you see white powdery patches on leaves? ").lower()
    wilting = input("Are plants wilting or drying from bottom? ").lower()
    insects = input("Do you see small insects on leaves or stem? ").lower()

    print("\n🔍 Diagnosing...\n")

    if crop == "rice":
        if yellow_leaves == "yes" and brown_spots == "yes":
            print("✅ Disease: Bacterial Leaf Blight")
            print("💊 Suggestion: Use copper-based fungicide and avoid waterlogging.")
        elif wilting == "yes" and insects == "yes":
            print("✅ Disease: Rice Stem Borer")
            print("💊 Suggestion: Use neem-based pesticide or carbofuran granules.")
        else:
            print("ℹ️ No major disease detected or symptoms unclear.")

    elif crop == "wheat":
        if white_patches == "yes":
            print("✅ Disease: Powdery Mildew")
            print("💊 Suggestion: Spray sulfur fungicide.")
        elif brown_spots == "yes":
            print("✅ Disease: Leaf Rust")
            print("💊 Suggestion: Use Mancozeb fungicide spray.")
        else:
            print("ℹ️ No major disease detected or symptoms unclear.")

    elif crop == "maize":
        if yellow_leaves == "yes" and brown_spots == "yes":
            print("✅ Disease: Turcicum Leaf Blight")
            print("💊 Suggestion: Apply Mancozeb.")
        elif wilting == "yes":
            print("✅ Disease: Downy Mildew")
            print("💊 Suggestion: Use Metalaxyl fungicide.")
        else:
            print("ℹ️ No major disease detected or symptoms unclear.")

    elif crop == "sugarcane":
        if wilting == "yes" and yellow_leaves == "yes":
            print("✅ Disease: Red Rot")
            print("💊 Suggestion: Remove infected clumps & treat seeds.")
        elif insects == "yes":
            print("✅ Disease: Sugarcane Shoot Borer")
            print("💊 Suggestion: Apply chlorpyrifos.")
        else:
            print("ℹ️ No major disease detected or symptoms unclear.")

    else:
        print("❌ Crop not recognized.")

    print("\n🌿 Nutrient Check:")
    if yellow_leaves == "yes":
        print("🌱 Suggestion: Leaves yellow — Apply Nitrogen fertilizer (like urea).")
    elif brown_spots == "yes":
        print("🌱 Suggestion: Brown spots — Apply Potassium fertilizer.")
    else:
        print("🌱 Plant looks healthy — no fertilizer required right now.")

    print("\n🌱 Thank you for using the Crop Disease Expert System!")

diagnose_crop()
